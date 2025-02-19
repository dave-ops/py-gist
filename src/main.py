"""
Module for Flattening Directory Structure and Uploading to GitHub Gist

This module contains functions to flatten the directory structure of a specified folder,
copy the first 3 files (for testing purposes) into a new flattened structure, and
upload these files to a GitHub Gist. It also includes user interaction for configuration
inputs and performs necessary validations like GitHub token validation.

Functions:
    - flatten: Flattens the directory structure by copying and sanitizing files.
    - upload_to_gist: Uploads the flattened files to a GitHub Gist.

Usage:
    - Run the script directly to prompt for configuration and execute the flattening and
      uploading process.
    - Import the module to use the `flatten` and `upload_to_gist` functions in other scripts.

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
from api import create_gist
from utils import (
    sanitize_filename,
    make_content_json_safe,
)


def flatten(folder_path, output_folder):
    """
    Flatten the directory structure of the given folder.

    This function walks through the specified folder, copies the first 3 files (for testing purposes),
    sanitizes their filenames, and places them into a new flattened structure in the output folder.

    Parameters
    ----------
    folder_path : str
        The path to the folder that needs to be flattened.
    output_folder : str
        The destination path where flattened files will be temporarily stored.

    Returns
    -------
    dict
        A dictionary where keys are the flattened filenames and values are dictionaries
        containing the 'content' of each file.
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

    return gist_files


def upload_to_gist(gist_files, gist_description, github_token):
    """
    Upload the flattened files to a GitHub Gist.

    This function takes the prepared files and uploads them to a GitHub Gist using the provided
    description and GitHub token for authentication.

    Parameters
    ----------
    gist_files : dict
        A dictionary containing the flattened filenames as keys and dictionaries with 'content' as values.
    gist_description : str
        A description for the Gist to be created.
    github_token : str
        The GitHub token for authentication to create the Gist.

    Returns
    -------
    None
        The function does not return anything but prints the status of the operation.
    """
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


def flatten_and_upload_to_gist(user_inputs):
    """
    Orchestrates the process of flattening a directory and uploading to GitHub Gist.

    This function uses the provided user inputs to flatten a directory structure and then upload
    the resulting files to a GitHub Gist.

    Parameters
    ----------
    user_inputs : dict
        A dictionary containing:
        - 'folder_path': Path to the folder to be flattened.
        - 'output_folder': Path where the flattened files will be stored.
        - 'gist_description': Description for the Gist.
        - 'github_token': GitHub token for authentication.

    Returns
    -------
    None
        The function does not return anything but prints the status of the operation.
    """
    folder_path = user_inputs["folder_path"]
    output_folder = user_inputs["output_folder"]
    gist_description = user_inputs["gist_description"]
    github_token = user_inputs["github_token"]

    gist_files = flatten(folder_path, output_folder)
    upload_to_gist(gist_files, gist_description, github_token)


if __name__ == "__main__":
    """
    Main execution block for the script. Handles user input for configuration
    and initiates the process to flatten a directory and upload to GitHub Gist.

    This block prompts the user for necessary paths, descriptions, and GitHub token,
    validates the token, checks the GitHub API connection, and then calls the main
    function to flatten and upload files.
    """
    # Assuming inputs.execute returns a dictionary with the required keys
    config_inputs = inputs.execute(os.getcwd())

    # run and upload
    flatten_and_upload_to_gist(config_inputs)
