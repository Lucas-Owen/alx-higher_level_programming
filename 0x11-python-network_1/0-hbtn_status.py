#!/usr/bin/python3
"""
This script fetches https://alx-intranet.hbtn.io/status and displays the body
"""


from urllib import request

with request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    body = response.read()
    print('Body response:')
    print(f'\t- type: {type(body)}')
    print(f'\t- content: {body}')
    print(f'\t- utf8 content: {body.decode()}')
