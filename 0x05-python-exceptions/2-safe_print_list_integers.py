#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    items_printed = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]))
            items_printed += 1
        except TypeError:
            break
    print()
    return items_printed
