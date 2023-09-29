#!/usr/bin/python3
"""
This is a script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter
"""


import requests
from sys import argv

head = {'Allow': 'application/json'}
data = {'q': argv[1]}
url = 'http://0.0.0.0:5000/search_user'

try:
    with requests.request('POST', url=url, headers=head, data=data) as resp:
        resp.raise_for_status()
        usr = resp.json()
        if usr:
            print(f'[{usr.get("id", None)}] {usr.get("name", None)}')
        else:
            print('No result')
except requests.exceptions.JSONDecodeError as err:
    print('Not a valid JSON')
