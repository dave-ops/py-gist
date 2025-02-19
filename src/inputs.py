"""
Module for Handling User Inputs and Configurations

This module manages the interaction with the user to gather necessary configuration inputs
for the GitHub Gist upload process. It includes functions to prompt for user input, validate
GitHub tokens, and perform preliminary checks on the GitHub API connection and rate limits.

Functions:
    - execute: Collects user inputs, validates them, and performs API checks.

Dependencies:
    - config: For configuration defaults and environment variable names.
    - utils: For utility functions like prompt_user and validate_github_token.
    - api: For functions to check GitHub API connection and rate limit.

Author:
    dave-ops

Date:
    2025-02-18

License:
    GNU
"""

import os
import config
from utils import (
    prompt_user,
    validate_github_token,
)
from api import check_api_connection, check_rate_limit

response_dict = {
    "folder_path": None,
    "output_folder": None,
    "gist_description": None,
    "github_token": None,
}


def execute(root):
    """
    Execute the user input collection process, including validation and API checks.

    This function prompts the user for configuration inputs related to the directory to flatten,
    output directory, Gist description, and GitHub token. It then validates the GitHub token
    and checks the GitHub API connection status and rate limit.

    Parameters
    ----------
    root : str
        The root directory from which default paths are constructed.

    Returns
    -------
    dict
        A dictionary containing:
        - 'folder_path': Path to the folder to be flattened.
        - 'output_folder': Path where the flattened files will be stored.
        - 'gist_description': Description for the Gist.
        - 'github_token': GitHub token for authentication.

    Raises
    ------
    ValueError
        If the GitHub token validation fails.
    """
    # Prompt user for input with default values
    response_dict["folder_path"] = prompt_user(
        "Enter the folder path to flatten",
        os.path.join(root, config.SOURCE_DIR_DEFAULT),
        config.ENV_VAR_SOURCE_DIR,
    )

    response_dict["output_folder"] = prompt_user(
        "Enter the output folder path",
        os.path.join(root, config.OUTPUT_DIR_DEFAULT),
        config.ENV_VAR_OUTPUT_DIR,
    )

    response_dict["gist_description"] = prompt_user(
        "Enter a description for the Gist",
        config.PROJECT_NAME_DEFAULT,
        config.ENV_VAR_PROJECT_NAME,
    )

    response_dict["github_token"] = prompt_user(
        "Enter your GitHub token",
        os.environ.get(config.ENV_VAR_GITHUB_TOKEN, ""),
        config.ENV_VAR_GITHUB_TOKEN,
    )

    # Validate GitHub token
    validate_github_token(response_dict["github_token"])

    # Check GitHub API connection
    print(f"Test GitHub API connection status code: {check_api_connection()}")

    # Check Rate Limit
    rate_limit_status = check_rate_limit(response_dict["github_token"])
    print(f"Rate Limit Status: {rate_limit_status}")

    return response_dict
