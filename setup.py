"""
Setup script for the py-gist project, which provides functionality to upload files to GitHub Gist.

This script configures the package for distribution, defining metadata like name, version, 
dependencies, and entry points for command-line usage.
"""

from setuptools import setup, find_packages

# Correctly using 'with' to open and read the README.md file
with open('docs/README.md', encoding='utf-8') as readme_file:
    long_description = readme_file.read()

setup(
    name='py-gist',
    # The name of the package as it will appear on PyPI.
    version='0.1',
    # The version of the package.
    packages=find_packages(include=['src', 'src.*']),
    # Finds all packages under the 'src' directory to include in the distribution.
    install_requires=[
        'requests',
    ],
    # Lists the dependencies required for this package to run. Here, 'requests' is needed for making HTTP requests.
    entry_points={
        'console_scripts': [
            'py-gist=src.main:main',
        ],
    },
    # Defines entry points for command-line scripts. 'py-gist' command will run the main function from src.main.
    author='dave-ops',
    # The author of the package.
    description='Upload files to Github Gist',
    # A brief description of what the package does.
    long_description=long_description,  # Use the variable defined with 'with' statement
    # Specifies that the long description is in Markdown format.
    long_description_content_type="text/markdown",
)
