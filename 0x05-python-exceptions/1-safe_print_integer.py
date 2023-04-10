#!/usr/bin/python3
def safe_print_integer(value):
    try:
        value > 0
        print("{:d}".format(value), end='')
        print()
        return True
    except Exception:
        return False
