#!/usr/bin/python3
"""
This script takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""


import requests
from requests.auth import HTTPBasicAuth
from sys import argv

username = argv[1]
token = argv[2]
auth = (username, token)
url = f'https://api.github.com/user'
headers = {
    'Accept': 'application/json',
    'X-GitHub-Api-Version': '2022-11-28'
}

try:
    with requests.get(url=url, headers=headers, auth=auth) as response:
        response.raise_for_status()
        print(response.json()['id'])
except Exception as e:
    print('None')
