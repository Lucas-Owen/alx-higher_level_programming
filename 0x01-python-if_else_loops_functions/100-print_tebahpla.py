#!/usr/bin/python3
str = ''
for i in range(27):
    str += chr(ord('z') - i - ((i % 2) * 32))
print(str)
