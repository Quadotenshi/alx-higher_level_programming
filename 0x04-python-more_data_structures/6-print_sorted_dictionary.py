#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    b = a_dictionary.items()
    for key, value in sorted(b):
        print("{} : {}".format(key, value))
