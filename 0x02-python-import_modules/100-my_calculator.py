#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    arg = len(sys.argv)
    op = sys.argv[2]

    if arg != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    elif op != "+" and op != "-" and op != "*" and op != "/":
        print("Unknown operator. Available operators: +, -, *, and /")
        sys.exit(1)
    else:
        a = sys.argv[1]
        b = sys.argv[3]
        if op == "+":
            result = add(int(a), int(b))
            print("{} + {} = {}".format(a, b, result))
        elif op == "-":
            result = sub(int(a), int(b))
            print("{} - {} = {}".format(a, b, result))
        elif op == "*":
            result = mul(int(a), int(b))
            print("{} * {} = {}".format(a, b, result))
        else:
            result = div(int(a), int(b))
            print("{} / {} = {}".format(a, b, result))
