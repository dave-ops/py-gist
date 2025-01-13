#!/bin/bash

# Set environment variables
export FOLDER_PATH="/path/to/your/folder/src"
export OUTPUT_FOLDER="./output_src"
export GIST_DESCRIPTION="pub-gob"

# Prompt for GitHub token
read -p "Enter your GitHub token: " GITHUB_TOKEN
export GITHUB_TOKEN

# Run the Python script
python main.py

# Wait for user input before closing
read -p "Press Enter to continue..."