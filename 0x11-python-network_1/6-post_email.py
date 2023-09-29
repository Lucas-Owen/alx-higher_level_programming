#!/usr/bin/python3
"""
This script takes in a URL and an email, sends a POST request to the passed URL
with the email as a parameter
and displays the body of the response (decoded in utf-8)
"""


import requests
from sys import argv

url = argv[1]
data = {'email': argv[2]}
with requests.request(method='POST', url=url, data=data) as response:
    body = response.text
    print(body)
