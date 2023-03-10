#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
digit = number % 10
string = "Last digit of "
not_six = "and is less than 6 but not 0"
five = "and is greater than 5"

if number < 0:
    digit = -(abs(number) % 10)
    if digit == 0:
        print("{}{} is 0 and is 0".format(string, number))
    else:
        print("{}{} is {} {}".format(string, number, digit, not_six))
else:
    digit = number % 10
    if digit > 5:
        print("Last digit of {} is {} {}".format(number, digit, five))
    elif digit == 0:
        print("Last digit of {} is {} and is 0".format(number, digit))
    else:
        print("Last digit of {} is {} {}".format(number, digit, not_six))
