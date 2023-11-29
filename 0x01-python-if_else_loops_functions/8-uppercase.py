#!/usr/bin/python3
def uppercase(str):
    for alpha in str:
        upper = alpha
        if (ord(upper) >= 97 and ord(upper) <= 122):
            upper = chr(ord(alpha) - 32)
        print("{}".format(upper), end='')
     print()
