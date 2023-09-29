#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL and
displays the value of the X-Request-Id variable found in the
header of the response
"""


if __name__ == "__main__":
    import requests
    from sys import argv

    with requests.get(argv[1]) as response:
        print(response.headers.get('X-Request-Id', None))
