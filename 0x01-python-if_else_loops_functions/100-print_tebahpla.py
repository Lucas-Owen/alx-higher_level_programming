#!/usr/bin/python3
for i in range(26):
    print(chr(ord('z') - i - ((i % 2) * 32)), end="")
