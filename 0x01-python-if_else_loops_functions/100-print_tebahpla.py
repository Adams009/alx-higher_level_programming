#!/usr/bin/python3
for upper in range(ord('z'), ord('a') - 1, -2):
    print("{}".format(chr(upper), chr(upper - 33)), end='')
