import os
import shutil
import time
from utils import (
    sanitize_filename,
    make_content_json_safe,
    prompt_user,
    validate_github_token,
)
from api import create_gist, check_api_connection, check_rate_limit
from config import (
    SOURCE_DIR_DEFAULT,
    OUTPUT_DIR_DEFAULT,
    PROJECT_NAME_DEFAULT,
    IGNORE_FOLDERS,
    ENV_VAR_SOURCE_DIR,
    ENV_VAR_OUTPUT_DIR,
    ENV_VAR_PROJECT_NAME,
    ENV_VAR_GITHUB_TOKEN,
)

def flatten_and_upload_to_gist(
    folder_path, 
    output_folder, 
    gist_description, 
    github_token
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
    for root, dirs, files in os.walk(folder_path):
        # Filter out directories to ignore
        dirs[:] = [d for d in dirs if d not in IGNORE_FOLDERS]

        for file in files[:3]:  # Limit to first 3 files for testing
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
    current_dir = os.getcwd()

    # Prompt user for input with default values
    folder_path = prompt_user(
        f"Enter the folder path to flatten",
        os.path.join(current_dir, SOURCE_DIR_DEFAULT),
        ENV_VAR_SOURCE_DIR,
    )

    output_folder = prompt_user(
        f"Enter the output folder path",
        os.path.join(current_dir, OUTPUT_DIR_DEFAULT),
        ENV_VAR_OUTPUT_DIR,
    )

    gist_description = prompt_user(
        f"Enter a description for the Gist", PROJECT_NAME_DEFAULT, ENV_VAR_PROJECT_NAME
    )

    github_token = prompt_user(
        f"Enter your GitHub token",
        os.environ.get(ENV_VAR_GITHUB_TOKEN, ""),
        ENV_VAR_GITHUB_TOKEN,
    )

    # Validate GitHub token
    validate_github_token(github_token)

    # Here, you would typically call functions to perform the rest of your script's logic
    print("Token validation passed. Proceed with your main logic here.")
    print(f"Test GitHub API connection status code: {check_api_connection()}")
    print(f"Rate Limit Status: {check_rate_limit(github_token)}")

    flatten_and_upload_to_gist(
        folder_path, output_folder, gist_description, github_token
    )