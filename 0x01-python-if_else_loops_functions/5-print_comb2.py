#!/usr/bin/python3

for i in range(100):
    print("{:0>2d}".format(i), end='')
    if (i + 1 != 100):
        print(",", end=" ")
