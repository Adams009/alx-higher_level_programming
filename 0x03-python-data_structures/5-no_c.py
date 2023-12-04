#!/usr/bin/python3
def no_c(my_string):
    copy_str = ""
    for n in my_string:
        if (n != 'c') and (n != 'C'):
            copy_str = copy_str + n
    return (copy_str)
