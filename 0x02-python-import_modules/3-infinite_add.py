#!/usr/bin/python3

import sys

a = 0
for i in range(1, len(sys.argv)):
    a += int(sys.argv[i])
    #print("{a}".format(a=sys.argv[i]))

print(a)
