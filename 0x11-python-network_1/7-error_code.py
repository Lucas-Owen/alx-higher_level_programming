#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8)
Handles urllib.error.HTTPError
"""


from sys import argv
import requests

url = argv[1]
try:
    with requests.get(url) as response:
        response.raise_for_status()
        body = response.text
        print(body)
except requests.exceptions.HTTPError as err:
    print(f'Error code: {err.response.status_code}')
