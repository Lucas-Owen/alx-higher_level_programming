#!/usr/bin/python3
"""
This is a script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter
"""


if __name__ == "__main__":
    import requests
    from sys import argv

    q = '' if len(argv) == 1 else argv[1]
    head = {'Allow': 'application/json'}
    data = {'q': q}
    url = 'http://0.0.0.0:5000/search_user'

    try:
        with requests.request('POST', url=url, headers=head, data=data) as res:
            res.raise_for_status()
            usr = res.json()
            if usr:
                print(f'[{usr.get("id", None)}] {usr.get("name", None)}')
            else:
                print('No result')
    except ValueError as err:
        print('Not a valid JSON')
