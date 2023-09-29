#!/usr/bin/python3
"""
This script takes in a URL and an email, sends a POST request to the passed URL
with the email as a parameter
and displays the body of the response (decoded in utf-8)
"""


from sys import argv
from urllib import request, parse

url = argv[1]
args = {'email': argv[2]}
data = parse.urlencode(args)
data = data.encode('ascii')
req = request.Request(url, data=data, method='POST')
with request.urlopen(req) as response:
    body = response.read()
    print(body.decode())
