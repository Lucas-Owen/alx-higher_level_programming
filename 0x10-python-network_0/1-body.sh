#!/bin/bash
# This bash script displays the body of a url passed as an argument
if (( "$#" == 1 )); then
    status="$(curl -sGI "$1" | grep HTTP | cut -d " " -f 2)"
    if (( "$status" == 200 )); then
        curl -sG "$1"
    fi
fi
