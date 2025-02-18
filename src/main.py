import os
import shutil
import time
from utils import sanitize_filename, make_content_json_safe
from api import create_gist, check_api_connection, check_rate_limit
from config import (SOURCE_DIR_DEFAULT, 
                    OUTPUT_DIR_DEFAULT, 
                    PROJECT_NAME_DEFAULT,
                    IGNORE_FOLDERS, 
                    ENV_VAR_SOURCE_DIR, 
                    ENV_VAR_OUTPUT_DIR,
                    ENV_VAR_PROJECT_NAME, 
                    ENV_VAR_GITHUB_TOKEN
                    )

def flatten_and_upload_to_gist(folder_path, output_folder, gist_description, github_token):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    gist_files = {}
    for root, dirs, files in os.walk(folder_path):
        # Filter out directories to ignore
        dirs[:] = [d for d in dirs if d not in IGNORE_FOLDERS]
        
        for file in files[:3]:  # Limit to first 3 files for testing
            relative_path = os.path.relpath(os.path.join(root, file), folder_path)
            flat_file_name = sanitize_filename(relative_path.replace(os.sep, '_'))
            source_path = os.path.join(root, file)
            destination_path = os.path.join(output_folder, flat_file_name)
            
            shutil.copy2(source_path, destination_path)
            
            with open(destination_path, 'r', encoding='utf-8') as file_content:
                content_raw = file_content.read()
                content = make_content_json_safe(content_raw)
                gist_files[flat_file_name] = {"content": content}
            
            print(f'Prepared for upload: {source_path} as {flat_file_name}')

    if not gist_files:
        print("No files were added to the Gist.")
        return

    print("Attempting to create Gist...")
    gist_url, success = create_gist(gist_files, gist_description, github_token)
    if success:
        print('Gist created successfully!')
        print(f'Gist URL: {gist_url}')
    else:
        print(gist_url)  # This will contain the error message

if __name__ == "__main__":
    current_dir = os.getcwd()
    
    # Prompt user for input with default values
    folder_path = input(f'Enter the folder path to flatten (default: {current_dir}\\{SOURCE_DIR_DEFAULT}): ') or os.path.join(current_dir, SOURCE_DIR_DEFAULT)
    os.environ[ENV_VAR_SOURCE_DIR] = folder_path

    output_folder = input(f'Enter the output folder path (default: {current_dir}\\{OUTPUT_DIR_DEFAULT}): ') or os.path.join(current_dir, OUTPUT_DIR_DEFAULT)
    os.environ[ENV_VAR_OUTPUT_DIR] = output_folder

    gist_description = input(f'Enter a description for the Gist (default: {PROJECT_NAME_DEFAULT}): ') or PROJECT_NAME_DEFAULT
    os.environ[ENV_VAR_PROJECT_NAME] = gist_description

    github_token = input(f'Enter your GitHub token ({os.environ.get(ENV_VAR_GITHUB_TOKEN)}): ') or os.environ.get(ENV_VAR_GITHUB_TOKEN)
    os.environ[ENV_VAR_GITHUB_TOKEN] = github_token

    # Validate GitHub token
    if not github_token:
        raise ValueError("GitHub token must not be empty.")

    print(f'Test GitHub API connection status code: {check_api_connection()}')
    print(f'Rate Limit Status: {check_rate_limit(github_token)}')

    flatten_and_upload_to_gist(folder_path, output_folder, gist_description, github_token)