#!/usr/bin/python3
def search_replace(my_list, search, replace):
    count = 0
    new = my_list[:]
    for i in my_list:
        count = count + 1
    for j in range(count):
        if search == my_list[j]:
            new[j] = replace
    return new
