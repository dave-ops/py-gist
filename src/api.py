import json
import requests
import os
from utils import make_content_json_safe


def create_gist(content, description, github_token):
    url = "https://api.github.com/gists"
    headers = {
        "Authorization": f"token {github_token.strip()}",
        "Accept": "application/vnd.github.v3+json",
        "Content-Type": "application/json",
    }
    data = {"description": description, "public": True, "files": content}

    json_data = make_content_json_safe(data)
    response = requests.post(url, headers=headers, data=json.dumps(json_data))

    if response.status_code == 201:
        return response.json()["html_url"], True
    else:
        return (
            f"Failed to create Gist. Status code: {response.status_code}. Error: {response.text}",
            False,
        )


def check_api_connection():
    response = requests.get("https://api.github.com")
    return response.status_code


def check_rate_limit(github_token):
    headers = {"Authorization": f"token {github_token}"}
    response = requests.get("https://api.github.com/rate_limit", headers=headers)
    return response.json()
