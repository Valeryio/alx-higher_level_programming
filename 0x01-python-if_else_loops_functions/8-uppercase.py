#!/usr/bin/python3

def uppercase(str):

    for i in range(len(str)):
        if (97 <= ord(str[i]) < 173):
            print("{n}".format(n=chr(ord(str[i]) - 32)}, end='')
        else:
            print("{n}".format(str[i]}), end='')
