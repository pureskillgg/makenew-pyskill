"""
Setup local Jupyter notebooks with local imports
"""
# pylint: disable=unused-import
# pylint: disable=wrong-import-position
from ..env_functions.env_setup import setup_env_from_dotenv, echo_paths


def setup_notebook(silent=False):
    setup_env_from_dotenv()
    if not silent:
        echo_paths()
