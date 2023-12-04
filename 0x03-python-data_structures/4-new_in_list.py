#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    count = 0
    new_list = my_list[:]
    for i in my_list:
        count += 1
    if 0 <= idx < count:
        new_list[idx] = element
        return new_list
    else:
        return my_list
