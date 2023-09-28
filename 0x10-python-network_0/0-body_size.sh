#!/bin/bash
# This bash script displays the content length of a request to a url passed as an argument
curl -sI "$1" | grep Content-Length | cut -d " " -f 2
