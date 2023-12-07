#!/usr/bin/python3
def common_elements(set_1, set_2):
    set11 = list(set_1)
    set22 = list(set_2)
    count = 0
    new = ""

    for i in set11:
        count += 1

    for l in range(count):
        if set11[l] == set22[l]:
            new = set11[l]

    return new
