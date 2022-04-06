"""
Functions for the tutorial analysis
"""
import pandas as pd


def aggregate_footsteps(df_footsteps) -> pd.DataFrame:
    """Count footsteps per player"""
    return (
        df_footsteps.groupby("player_id_fixed", as_index=False)
        .size()
        .rename(columns={"size": "steps"})
    )


def simplify_player_info(df_player_info) -> pd.DataFrame:
    """Extract rank, wins, and friendly commends per player"""
    return (
        df_player_info[["player_id_fixed", "commends_friendly", "wins", "rank"]]
        .groupby("player_id_fixed", as_index=False)
        .max()
    )


def get_map_name(df_header) -> str:
    """Extract map name"""
    return df_header["map_name"].iat[0]


def assemble_final_df(df_footsteps_total, df_pi_simple, map_name) -> pd.DataFrame:
    """Assemble each piece into the final dataframe"""
    df_final = pd.merge(
        df_footsteps_total, df_pi_simple, how="left", on="player_id_fixed"
    )
    df_final["map_name"] = map_name
    return df_final
