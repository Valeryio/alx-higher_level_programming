#!/usr/bin/python3

def pow(a, b):

    base = a
    exp = b

    if (b == 0):
        return 1

    if (b < 0):
        b *= -1

    for i in range(1, b):
        a *= base

    if (exp > 0):
        return a

    elif (exp < 0):
        return (float(1 / a))
