#!/usr/bin/python3

i = 122

while i <= 97:
    print("{}{}".format(chr(i), chr(i - 1).upper()), end='')
    i -= 2
