#!/usr/bin/python3
"""
This script fetches https://alx-intranet.hbtn.io/status and displays the body
"""


import requests

with requests.get('https://alx-intranet.hbtn.io/status') as response:
    body = response.text
    print('Body response:')
    print(f'    - type: {type(body)}')
    print(f'    - content: {body}')
