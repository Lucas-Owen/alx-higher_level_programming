#!/bin/bash
# Sends a delete request to the url passed in as argument and displays the body of the response
if (( "$#" == 1 )); then
    curl -s -X DELETE "$1"
fi
