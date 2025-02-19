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
