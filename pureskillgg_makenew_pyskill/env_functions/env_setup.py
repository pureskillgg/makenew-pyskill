"""
Setup env vars
"""
import os
from dotenv import load_dotenv

ENV_PREFIX = "pureskillgg_tome"


def setup_env_from_dotenv():
    """
    Load ../.env into system environment
    """
    load_dotenv(os.path.join("..", ".env"))


def echo_paths():
    """
    Print out relevant env info for tome-related variables
    """
    echo("default_header_name")
    echo("ds_type")
    echo("collection_path")
    echo("ds_collection_path")


def echo(name):
    """
    Print out env info
    """
    var, full_name = get_env_var(name)
    if var is None:
        print(full_name, "is not setup")
    else:
        print(full_name, "is", var)


def get_env_var(name):
    """
    Helper to get environment variables
    """
    key = "_".join([ENV_PREFIX, name]).upper()
    return os.environ.get(key), key
