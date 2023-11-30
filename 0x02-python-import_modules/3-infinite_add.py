#!/usr/bin/python3

import sys

argument_take = sys.argv[1:]

argument_len = len(argument_take)

if (argument_len < 1):
    print(0)

else:
    for it in range(argument_len):
        total= map(int,argument_take)
        result = sum(total)

    print("{}".format(result))

if __name__ == "__main__":
    pass
