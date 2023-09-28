#!/bin/bash
# Sends a delete request to the url passed in as argument and displays the body of the response
curl -sI -X OPTIONS "$1" | grep Allow | cut -d " " -f 2-
