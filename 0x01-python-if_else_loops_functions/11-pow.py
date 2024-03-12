#!/usr/bin/python3

def pow(a, b):

    base = a
    for i in range(1, b):
        a *= base
    return a
