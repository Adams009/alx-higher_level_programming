def safe_print_list(my_list=[], x=0):
    c = 0
    for datas in my_list:
        if c < x:
            print(datas, end="")
            c = c + 1

    except IndexERROR:
        break
