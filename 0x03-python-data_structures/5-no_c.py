#!/usr/bin/env python3
def no_c(my_string):
    copy_str = ""
    if my_string is None:
        return
    else:
        for n in my_string:
            if (n != 'c' and n != 'C'):
                copy_str += n
        return copy_str
