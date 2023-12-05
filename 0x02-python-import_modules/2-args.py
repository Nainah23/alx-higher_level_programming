#!/usr/bin/python3

if __name__ == "__name__":
    import sys

    arg = sys.argv
    size = len(arg) - 1

    if argc > 1:
        print("{} arguments:".format(size))
        for a in range(1, size + 1):
            print("{}: {}".format(i, (arg[a])))

    elif argc == 0:
        print("{} arguments:".format(size))
    else:
        print("{} arguments:".format(size))
        print("{}: {}".format(size, (arg[1])))
