#!/usr/bin/python3
"""
Please list 10 commits (from the most recent to oldest) of a
repository by a user passed in as arguments
You must use the GitHub API, here is the documentation
https://developer.github.com/v3/repos/commits/
Print all commits by: `<sha>: <author name>` (one by line)
"""


if __name__ == "__main__":
    from sys import argv
    import requests
    repo = argv[1]
    owner = argv[2]
    url = f'https://api.github.com/repos/{owner}/{repo}/commits'
    headers = {
        'X-GitHub-Api-Version': '2022-11-28',
        'Accept': 'application/vnd.github+json'
    }
    params = {
        'page': 1,
        'per_page': 10
    }
    with requests.get(url=url, params=params, headers=headers) as response:
        for commit in response.json():
            print(f'{commit["sha"]}: {commit["commit"]["author"]["name"]}')
