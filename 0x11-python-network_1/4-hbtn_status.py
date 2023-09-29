#!/usr/bin/python3
"""
This script fetches https://alx-intranet.hbtn.io/status and displays the body
"""


if __name__ == "__main__":
    import requests

    with requests.get('https://alx-intranet.hbtn.io/status') as response:
        body = response.text
        print('Body response:')
        print(f'\t- type: {type(body)}')
        print(f'\t- content: {body}')
