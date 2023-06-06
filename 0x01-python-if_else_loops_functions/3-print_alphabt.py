#!/usr/bin/python3
for i in range(26):
    if ord('a') + i == ord('e') or ord('a') + i == ord('q'):
        continue
    print('{}'.format(chr(ord('a') + i)), end="")
