

import requests


def get_github_description(github_url):
    api_url = github_url.replace("github.com/", "api.github.com/repos/")
    return requests.get(api_url).json()["description"]


def test_get_github_description():
    github_url = "https://github.com/umihico/pypienv"
    description = get_github_description(github_url)
    print(description)
    assert "selenium" in description.lower()
