#!/bin/bash
# Sends a delete request to the url passed in as argument and displays the body of the response
curl -s -X DELETE "$1"
