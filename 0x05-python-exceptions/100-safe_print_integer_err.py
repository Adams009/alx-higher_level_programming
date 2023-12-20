#!/usr/bin/python3

def safe_print_integer_err(value):
    integer = True
    try:
        print("{:d}".format(value))
    except:
        print'Exception:', e, file=sys.stderr)
        integer = False
    return integer
