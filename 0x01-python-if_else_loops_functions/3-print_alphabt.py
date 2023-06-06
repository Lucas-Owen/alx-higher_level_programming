#!/usr/bin/python3
for i in range(27):
    if ord('a') + i == ord('e') or ord('a') + i == ord('q'):
        continue
    print(chr(ord('a') + i), end="")
