#!/usr/bin/python3

def uppercase(str):

    for i in range(len(str)):
        if (97 <= ord(str[i]) < 173):
            print(f"{chr(ord(str[i]) - 32)}", end='')
        else:
            print(f"{str[i]}", end='')
