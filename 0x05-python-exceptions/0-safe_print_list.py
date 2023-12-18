def safe_print_list(my_list=[], x=0):
    c = 0
    for datas in range(x):
        try:
            print("{}".format(my_list[datas], end="")
            c = c + 1
        except IndexError:
            break
    print("")
    return (c)
