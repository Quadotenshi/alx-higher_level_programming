#!/usr/bin/python3

def uppercase(str):
    for i in range(len(str)):
        x = ord(str[i])
        if x >= 97:
            x -= 32
        print(chr(x), end='')
    print()
