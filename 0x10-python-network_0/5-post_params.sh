#!/bin/bash
# A Bash script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response
# A variable email must be sent with the value test@gmail.com
# A variable subject must be sent with the value 'I will always be here for PLD'

if (( "$#" == 1 )); then
    curl -sG -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1"
fi
