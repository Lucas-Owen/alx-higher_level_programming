#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8)
Handles urllib.error.HTTPError
"""


from sys import argv
from urllib import request, error

url = argv[1]
try:
    with request.urlopen(url) as response:
        body = response.read()
        print(body.decode())
except error.HTTPError as err:
    print(f'Error code: {err.code}')
