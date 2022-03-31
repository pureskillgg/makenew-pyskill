"""
Setup local Jupyter notebooks with local imports
"""

from ..env_functions.env_setup import setup_env_from_dotenv, echo_paths


def setup_notebook(silent=False):
    """Setup notebook environment"""
    setup_env_from_dotenv()
    if not silent:
        echo_paths()
