#!/usr/bin/python3

import sys

if __main__=="__main__":

    a = 0

    for i in range(1, len(sys.argv)):
        a += int(sys.argv[i])

    print(a)
