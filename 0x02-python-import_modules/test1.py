#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":

    if (len(argv) >= 3):
        print("{}: arguments:".format(len(sys.argv) - 1))
    elif (len(sys.argv) == 1):
        print("{} arguments.".format(len(sys.argv) - 1))
    else:
        print("{}: argument:".format(len(sys.argv) - 1))

    for i in range(1, len(sys.argv)):
        print("{}: {}".format(i, sys.argv[i]))
