#!/usr/bin/python3

import sys

print("{a}: argument".format(a=len(sys.argv) - 1))
for i in range(1, len(sys.argv)):
    print("{a}: {b}".format(a=i, b=sys.argv[i]))
