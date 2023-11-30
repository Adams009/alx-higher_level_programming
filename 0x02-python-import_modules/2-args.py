#!/usr/bin/python3

import sys

argument_take = sys.argv[1:]

argument_length = len(argument_take)

if (argument_length < 1):
    print("0 arguments.")

else:
    if (argument_length == 1):
        plural = ''
    else:
        plural = 's'

    print("{} argument{}:".format(argument_length, plural))

    for it in range(argument_length):
        print("{}: {}".format(it + 1, argument_take[it]))

if __name__ == "__main__":
    pass
