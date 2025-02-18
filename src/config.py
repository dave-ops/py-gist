# config.py
import os

# Default values
SOURCE_DIR_DEFAULT = "src"
OUTPUT_DIR_DEFAULT = "output"
PROJECT_NAME_DEFAULT = "py-gist"

# Gist settings
PROJECT_NAME_DEFAULT = "py-gist"

# Ignore folders
IGNORE_FOLDERS = ["__pycache__"]

# Environment variable names
ENV_VAR_SOURCE_DIR = "SOURCE_DIR"
ENV_VAR_OUTPUT_DIR = "OUTPUT_DIR"
ENV_VAR_PROJECT_NAME = "PROJECT_NAME"
ENV_VAR_GITHUB_TOKEN = "GITHUB_TOKEN"


# Function to get environment variable or default value
def get_env_or_default(env_var, default_value):
    return os.environ.get(env_var, default_value)
