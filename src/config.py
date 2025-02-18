"""
Configuration settings for the py-gist project.

This module defines default values for source and output directories, project name,
ignored folders, and environment variable names. It also includes a utility function 
to retrieve environment variables with fallback to default values.
"""

import os

# Default values
SOURCE_DIR_DEFAULT = "src"
OUTPUT_DIR_DEFAULT = "output"
PROJECT_NAME_DEFAULT = "py-gist"

# Ignore folders
IGNORE_FOLDERS = ["__pycache__"]

# Environment variable names
ENV_VAR_SOURCE_DIR = "SOURCE_DIR"
ENV_VAR_OUTPUT_DIR = "OUTPUT_DIR"
ENV_VAR_PROJECT_NAME = "PROJECT_NAME"
ENV_VAR_GITHUB_TOKEN = "GITHUB_TOKEN"


def get_env_or_default(env_var, default_value):
    """
    Retrieve an environment variable or return a default value if not set.

    Parameters
    ----------
    env_var : str
        The name of the environment variable to retrieve.
    default_value : str
        The default value to return if the environment variable is not set.

    Returns
    -------
    str
        The value of the environment variable if it exists, otherwise the default value.
    """
    return os.environ.get(env_var, default_value)
