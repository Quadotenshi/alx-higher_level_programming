#!/usr/bin/python3
if __name__ == "__main__":
    import hidden.py

    dirs = dir(hidden.py)

    for i in dirs:
        if i[:2] != "__":
            print("{}".format(i))
