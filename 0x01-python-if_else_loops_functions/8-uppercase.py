#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord(c) <= ord('z') and ord(c) >= ord('a'):
            c = chr(ord('A') + ord(c) - ord('a'))
        print(c, end="")
    print()
