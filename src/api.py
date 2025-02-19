"""
Module for interacting with the GitHub API to create Gists and check API status.

This module contains functions for creating public GitHub Gists, checking the connection
to the GitHub API, and querying the API rate limit. It requires GitHub authentication
via a token for some operations.
"""

import json
import requests
from utils import make_content_json_safe


def create_gist(content, description, github_token):
    """
    Create a new public GitHub Gist with the provided content.

    This function sends a POST request to the GitHub API to create a new Gist.
    It uses the provided GitHub token for authentication.

    Parameters
    ----------
    content : dict
        A dictionary where keys are filenames and values are dictionaries
        containing a 'content' key with the file's content.
    description : str
        A description for the Gist.
    github_token : str
        The GitHub token for API authentication.

    Returns
    -------
    tuple
        A tuple containing:
        - str: The URL of the created Gist if successful, or an error message.
        - bool: True if the Gist was created successfully, False otherwise.

    Raises
    ------
    requests.RequestException
        If there's an error in making the HTTP request.
    """
    url = "https://api.github.com/gists"
    headers = {
        "Authorization": f"token {github_token.strip()}",
        "Accept": "application/vnd.github.v3+json",
        "Content-Type": "application/json",
    }
    data = {"description": description, "public": True, "files": content}

    json_data = make_content_json_safe(data)
    response = requests.post(
        url, headers=headers, data=json.dumps(json_data), timeout=10
    )

    if response.status_code == 201:
        return response.json()["html_url"], True
    return (
        f"Failed to create Gist. Status code: {response.status_code}. Error: {response.text}",
        False,
    )


def check_api_connection():
    """
    Check the connection to the GitHub API.

    This function sends a GET request to the GitHub API root endpoint to verify
    if the connection is working.

    Returns
    -------
    int
        The HTTP status code of the response, indicating the connection status.

    Raises
    ------
    requests.RequestException
        If there's an error in making the HTTP request.
    """
    response = requests.get("https://api.github.com", timeout=10)
    return response.status_code


def check_rate_limit(github_token):
    """
    Check the GitHub API rate limit for the authenticated user.

    This function retrieves the rate limit status from the GitHub API using
    the provided GitHub token.

    Parameters
    ----------
    github_token : str
        The GitHub token for API authentication.

    Returns
    -------
    dict
        A dictionary containing rate limit information from the GitHub API.

    Raises
    ------
    requests.RequestException
        If there's an error in making the HTTP request.
    """
    headers = {"Authorization": f"token {github_token}"}
    response = requests.get(
        "https://api.github.com/rate_limit", headers=headers, timeout=10
    )
    return response.json()
