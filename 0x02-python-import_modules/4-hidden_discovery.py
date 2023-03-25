#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    dirs = dir(hidden_4)

    dirs.sort()
    for i in dirs:
        if i[:2] != "__":
            print("{}".format(i))
