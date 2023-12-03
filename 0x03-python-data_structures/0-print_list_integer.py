#!/usr/bin/python3
def print_list_integer(my_list=[]):
    count = 0
    new_list = []
    for integer in my_list:
        count = count + 1
    for i in range(count):
        print("{}".format(my_list[i]))
