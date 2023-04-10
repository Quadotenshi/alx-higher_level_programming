#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        splited_list = my_list[:x]
        for item in splited_list:
            if item:
                count = count + 1
            print("{:d}".format(item), end='')
        print()
        return count
    except Exception:
        print("Something went wrong")
