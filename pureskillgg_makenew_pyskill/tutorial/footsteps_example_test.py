# pylint: disable=missing-docstring

from pathlib import Path

import pytest

from pureskillgg_dsdk import DsReaderFs, GameDsLoader

from .footsteps_example import (
    aggregate_footsteps,
    assemble_final_df,
    get_map_name,
    simplify_player_info,
)

SAMPLE_DATA = Path(__file__).parents[2] / "sample_data"
PREMIER_MATCH = "csds/2026/10/09/83d933c3-11a6-43fb-b368-8fd429f350af/csds"
FACEIT_MATCH = "csds/2026/10/09/6fddf4fa-8f78-4958-8cc0-499bc844e29f/csds"
INSTRUCTIONS = [
    {"channel": "player_footstep", "columns": ["player_id_fixed"]},
    {
        "channel": "player_info",
        "columns": ["player_id_fixed", "wins", "rank", "rank_type"],
    },
    {"channel": "header"},
]


def load(manifest_key):
    reader = DsReaderFs(root_path=str(SAMPLE_DATA), manifest_key=manifest_key)
    return GameDsLoader(reader=reader).get_channels(INSTRUCTIONS)


@pytest.fixture(name="premier", scope="module")
def fixture_premier():
    return load(PREMIER_MATCH)


@pytest.fixture(name="faceit", scope="module")
def fixture_faceit():
    return load(FACEIT_MATCH)


def test_aggregate_footsteps_counts_every_step(premier):
    steps = aggregate_footsteps(premier["player_footstep"])
    assert list(steps.columns) == ["player_id_fixed", "steps"]
    assert steps["steps"].sum() == len(premier["player_footstep"])
    assert steps["player_id_fixed"].is_unique


def test_simplify_player_info_keeps_one_row_per_player(premier):
    info = simplify_player_info(premier["player_info"])
    assert list(info.columns) == ["player_id_fixed", "wins", "rank", "rank_type"]
    assert info["player_id_fixed"].is_unique
    assert len(info) == 10


def test_premier_ranks_are_cs_ratings(premier):
    info = simplify_player_info(premier["player_info"])
    assert set(info["rank_type"]) == {11}
    assert info["rank"].max() > 1000


def test_faceit_players_have_no_rank(faceit):
    info = simplify_player_info(faceit["player_info"])
    assert set(info["rank_type"]) == {-1}
    assert set(info["rank"]) == {0}


def test_get_map_name(premier, faceit):
    assert get_map_name(premier["header"]) == "de_ancient"
    assert get_map_name(faceit["header"]) == "de_anubis"


def test_assemble_final_df_keeps_every_player_with_steps(premier):
    steps = aggregate_footsteps(premier["player_footstep"])
    info = simplify_player_info(premier["player_info"])
    final = assemble_final_df(steps, info, "de_ancient")
    assert len(final) == len(steps)
    assert set(final.columns) == {
        "player_id_fixed",
        "steps",
        "wins",
        "rank",
        "rank_type",
        "map_name",
    }
    assert (final["map_name"] == "de_ancient").all()
