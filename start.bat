@echo off
set FOLDER_PATH=C:\dev\repos\pub-gob\src
set OUTPUT_FOLDER=.\output_src
set GIST_DESCRIPTION=pub-gob

set /p GITHUB_TOKEN=YOUR_GITHUB_TOKEN 

python main.py

pause