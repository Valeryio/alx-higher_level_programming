#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":

    if (len(argv) >= 3):
        print("{} arguments:".format(len(argv) - 1))
    elif (len(argv) == 1):
        print("{} arguments.".format(len(argv) - 1))
    elif (len(argv) == 2):
        print("{} argument:".format(len(argv) - 1))
    else:
        pass

    for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[i]))
