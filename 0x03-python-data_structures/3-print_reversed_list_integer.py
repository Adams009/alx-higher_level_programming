#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    count = 0
    for i in my_list:
        count += 1
    length = count - 1
    while length >= 0:
        print("{:d}".format(my_list[length]))
        length -= 1
