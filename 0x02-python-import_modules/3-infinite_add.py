#!/usr/bin/python3

import sys

argument_take = sys.argv[1:]

argument_len = len(argument_take)

if (argument_len < 1):
    print('0')

else:
    result = sum(int(k) for k in argument_take)

    print("{}".format(result))

if __name__ == "__main__":
    pass
