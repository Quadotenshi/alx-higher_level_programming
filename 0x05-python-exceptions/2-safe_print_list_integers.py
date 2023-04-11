#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    new_list = []
    count = 0
    try:
        last = my_list[x - 1]
        for i in my_list[:x]:
            if type(i) == int:
                new_list.append(i)
                count += 1
        for i in new_list:
            print("{:d}".format(i), end='')
        print()
        return count
    except Exception:
        print("Error")
