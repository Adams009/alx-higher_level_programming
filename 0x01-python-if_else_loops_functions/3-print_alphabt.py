#!/usr/bin/python3
for ascii_lower in range(97, 123):
    if (chr(ascii_lower) not in ['q', 'e']):
        print("{}".format(chr(ascii_lower)), end='')
