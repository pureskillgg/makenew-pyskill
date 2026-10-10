# pylint: disable=missing-docstring
"""
Run the tutorial notebooks 1 to 6 and the template notebook, in order, on the sample data.

Each run works in a copy of notebooks/ and sample_data/, so it never touches
your own .env or tomes. Notebook 7 needs an AWS Data Exchange subscription,
so it isn't run here.
"""

import os
import shutil
from pathlib import Path

import nbformat
import pytest
from nbclient import NotebookClient

REPO = Path(__file__).parents[1]
TUTORIAL = [
    "1 - Setup.ipynb",
    "2 - The sample data.ipynb",
    "3 - Make header tome.ipynb",
    "4 - Do datascience exploration.ipynb",
    "5 - Create tome.ipynb",
    "6 - Train data science models.ipynb",
]


@pytest.fixture(name="workspace", scope="module")
def fixture_workspace(tmp_path_factory):
    root = tmp_path_factory.mktemp("repo")
    shutil.copytree(
        REPO / "notebooks",
        root / "notebooks",
        ignore=shutil.ignore_patterns(".env", ".ipynb_checkpoints"),
    )
    shutil.copytree(REPO / "sample_data", root / "sample_data")
    saved = {
        k: os.environ.pop(k)
        for k in list(os.environ)
        if k.startswith("PURESKILLGG_TOME_")
    }
    os.environ["MPLBACKEND"] = "Agg"
    yield root
    os.environ.update(saved)


def run(path):
    notebook = nbformat.read(path, as_version=4)
    NotebookClient(
        notebook,
        timeout=600,
        kernel_name="python3",
        resources={"metadata": {"path": str(path.parent)}},
    ).execute()
    return notebook


def outputs(notebook):
    text = []
    for cell in notebook.cells:
        for out in cell.get("outputs", []):
            text.append(
                out.get("text", "") or str(out.get("data", {}).get("text/plain", ""))
            )
    return "\n".join(text)


def test_tutorial_runs_in_order(workspace):
    results = {}
    for name in TUTORIAL:
        results[name] = outputs(run(workspace / "notebooks" / "tutorial" / name))
    assert "PURESKILLGG_TOME_DS_COLLECTION_PATH=" in results["1 - Setup.ipynb"]
    assert "4 matches in" in results["2 - The sample data.ipynb"]
    assert "42 channels" in results["2 - The sample data.ipynb"]
    assert "There are 4 matches in the header." in results["3 - Make header tome.ipynb"]
    assert "4 matches," in results["5 - Create tome.ipynb"]
    assert "Premier players" in results["6 - Train data science models.ipynb"]
    graded = results["6 - Train data science models.ipynb"]
    assert "you got a good grade" in graded or "get gud kid" in graded


def test_template_runs(workspace):
    # The tutorial's notebook 1 wrote notebooks/.env, which the template reads
    if not (workspace / "notebooks" / ".env").exists():
        run(workspace / "notebooks" / "tutorial" / TUTORIAL[0])
    text = outputs(run(workspace / "notebooks" / "template" / "template.ipynb"))
    assert "duck_share" in text
