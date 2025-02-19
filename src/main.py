"""
Module for Flattening Directory Structure and Uploading to GitHub Gist

This module contains functions to flatten the directory structure of a specified folder,
copy the first 3 files (for testing purposes) into a new flattened structure, and
upload these files to a GitHub Gist. It also includes user interaction for configuration
inputs and performs necessary validations like GitHub token validation.

Functions:
    - flatten_and_upload_to_gist: Flattens a directory and uploads files to a Gist.

Usage:
    - Run the script directly to prompt for configuration and execute the flattening and
      uploading process.
    - Import the module to use the `flatten_and_upload_to_gist` function in other scripts.

Version:
    1.0

Author:
    dave-ops

Date:
    2025-02-18

License:
    GNU
"""

import os
import shutil
import config
import inputs
from utils import (
    sanitize_filename,
    make_content_json_safe,
    prompt_user,
    validate_github_token,
)
from api import create_gist, check_api_connection, check_rate_limit


def flatten_and_upload_to_gist(
    folder_path, output_folder, gist_description, github_token
):
    """
    Flatten the directory structure of given folder and upload files to a GitHub Gist.

    This function takes a folder, flattens its structure by copying the first 3 files
    (for testing purposes), sanitizes their filenames, and uploads them to a GitHub Gist.

    Parameters
    ----------
    folder_path : str
        The path to the folder that needs to be flattened and uploaded.
    output_folder : str
        The destination path where flattened files will be temporarily stored.
    gist_description : str
        A description for the Gist to be created.
    github_token : str
        The GitHub token for authentication to create the Gist.

    Returns
    -------
    None
        The function does not return anything but prints the status of the operation.
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    gist_files = {}
    file_count = 0
    for root, dirs, files in os.walk(folder_path):
        # Filter out directories to ignore
        dirs[:] = [d for d in dirs if d not in config.IGNORE_FOLDERS]

        for file in files:
            if file_count >= 3:  # Limit to first 3 files for testing
                break
            relative_path = os.path.relpath(os.path.join(root, file), folder_path)
            flat_file_name = sanitize_filename(relative_path.replace(os.sep, "_"))
            source_path = os.path.join(root, file)
            destination_path = os.path.join(output_folder, flat_file_name)

            shutil.copy2(source_path, destination_path)

            with open(destination_path, "r", encoding="utf-8") as file_content:
                content_raw = file_content.read()
                content = make_content_json_safe(content_raw)
                gist_files[flat_file_name] = {"content": content}

            print(f"Prepared for upload: {source_path} as {flat_file_name}")
            file_count += 1

    if not gist_files:
        print("No files were added to the Gist.")
        return

    print("Attempting to create Gist...")
    gist_url, success = create_gist(gist_files, gist_description, github_token)
    if success:
        print("Gist created successfully!")
        print(f"Gist URL: {gist_url}")
    else:
        print(gist_url)  # This will contain the error message


if __name__ == "__main__":
    """
    Main execution block for the script. Handles user input for configuration
    and initiates the process to flatten a directory and upload to GitHub Gist.

    This block prompts the user for necessary paths, descriptions, and GitHub token,
    validates the token, checks the GitHub API connection, and then calls the main
    function to flatten and upload files.
    """
    responses = inputs.execute(os.getcwd())

    flatten_and_upload_to_gist(
        responses["folder_path"],
        responses["output_folder"],
        responses["gist_description"],
        responses["github_token"],
    )
