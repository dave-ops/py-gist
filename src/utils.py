"""
Module for Utility Functions

This module contains various utility functions used throughout the application for tasks like
sanitizing filenames, escaping JSON content, prompting for user input, and validating GitHub tokens.

Functions:
    - json_safe: Escapes special characters in strings for JSON safety.
    - make_content_json_safe: Recursively makes dictionary or list content JSON safe.
    - sanitize_filename: Sanitizes filenames by replacing invalid characters with underscores.
    - prompt_user: Prompts the user for input with a default value and sets an environment variable.
    - validate_github_token: Validates that a GitHub token is not empty.

Usage:
    - These functions are intended to be imported and used in other parts of the application.

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
import re


def json_safe(s):
    """
    Make a string JSON safe by escaping special characters.

    This function ensures that a string can be safely included in JSON by escaping special characters
    like backslashes, newlines, tabs, etc., and handling non-ASCII characters.

    Parameters
    ----------
    s : str
        The string to make JSON safe.

    Returns
    -------
    str
        The JSON-safe version of the input string.
    """
    if isinstance(s, str):
        # Escape special characters
        s = s.replace("\\", "\\\\")  # Backslash
        s = s.replace("\n", "\\n")  # Newline
        s = s.replace("\r", "\\r")  # Carriage return
        s = s.replace("\t", "\\t")  # Tab
        s = s.replace("\b", "\\b")  # Backspace
        s = s.replace("\f", "\\f")  # Form feed
        s = s.replace('"', '\\"')  # Double quote
        # Handle non-ASCII characters
        return s.encode("utf-8").decode("unicode_escape")
    return s


def make_content_json_safe(content):
    """
    Recursively make content JSON safe for dictionaries, lists, or strings.

    This function applies json_safe to strings, and recursively to dictionaries and lists to ensure
    all nested content is JSON safe.

    Parameters
    ----------
    content : dict, list, str, or any
        The content to make JSON safe. Can be a dictionary, list, string, or any other type.

    Returns
    -------
    dict, list, str, or any
        The JSON-safe version of the input content, maintaining its structure.
    """
    if isinstance(content, dict):
        return {json_safe(k): make_content_json_safe(v) for k, v in content.items()}
    if isinstance(content, list):
        return [make_content_json_safe(item) for item in content]
    if isinstance(content, str):
        return json_safe(content)
    return content


def sanitize_filename(filename):
    """
    Sanitize a filename by replacing invalid characters with underscores.

    This function uses a regular expression to replace any character that is not a word character,
    underscore, or dot with an underscore, ensuring the filename is safe for most file systems.

    Parameters
    ----------
    filename : str
        The filename to sanitize.

    Returns
    -------
    str
        The sanitized filename.
    """
    return re.sub(r"[^\w_.]", "_", filename)


def prompt_user(prompt, default_value, env_var_name):
    """
    Prompt the user for input with a default value and set the environment variable.

    :param prompt: The prompt to display to the user
    :param default_value: The default value if the user doesn't enter anything
    :param env_var_name: The name of the environment variable to set
    :return: The user's input or the default value
    """
    user_input = input(f"{prompt} (default: {default_value}): ") or default_value
    os.environ[env_var_name] = user_input
    return user_input


def validate_github_token(token):
    """
    Validate that the GitHub token is not empty.

    This function checks if the provided GitHub token is empty. If it is, it raises a ValueError.

    Parameters
    ----------
    token : str
        The GitHub token to validate.

    Raises
    ------
    ValueError
        If the token is empty.
    """
    if not token:
        raise ValueError("GitHub token must not be empty.")
