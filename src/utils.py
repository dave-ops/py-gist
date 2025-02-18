import os
import re

def json_safe(s):
    if isinstance(s, str):
        # Escape special characters
        s = s.replace('\\', '\\\\')  # Backslash
        s = s.replace('\n', '\\n')   # Newline
        s = s.replace('\r', '\\r')   # Carriage return
        s = s.replace('\t', '\\t')   # Tab
        s = s.replace('\b', '\\b')   # Backspace
        s = s.replace('\f', '\\f')   # Form feed
        s = s.replace('"', '\\"')    # Double quote
        # Handle non-ASCII characters
        return s.encode('utf-8').decode('unicode_escape')
    return s

def make_content_json_safe(content):
    if isinstance(content, dict):
        return {json_safe(k): make_content_json_safe(v) for k, v in content.items()}
    elif isinstance(content, list):
        return [make_content_json_safe(item) for item in content]
    elif isinstance(content, str):
        return json_safe(content)
    else:
        return content

def sanitize_filename(filename):
    return re.sub(r'[^\w_.]', '_', filename)

def prompt_user(prompt, default_value, env_var_name):
    """
    Prompt the user for input with a default value and set the environment variable.

    :param prompt: The prompt to display to the user
    :param default_value: The default value if the user doesn't enter anything
    :param env_var_name: The name of the environment variable to set
    :return: The user's input or the default value
    """
    user_input = input(f'{prompt} (default: {default_value}): ') or default_value
    os.environ[env_var_name] = user_input
    return user_input

def validate_github_token(token):
    """Validate that the GitHub token is not empty."""
    if not token:
        raise ValueError("GitHub token must not be empty.")