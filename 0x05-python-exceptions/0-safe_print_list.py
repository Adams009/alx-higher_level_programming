def safe_print_list(my_list=[], x=0):
    try:
        c = 0

        for datas in my_list:
            if c < x:
                print(datas, end="")
                c = c + 1

            else:
                break
        print()

        return (c)

    except Expection as e:
        print(f"An error occurred: {e}")

        return (0)
