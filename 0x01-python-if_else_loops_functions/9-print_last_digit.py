#!/usr/bin/python3

def print_last_digit(number):

    try:
        print(f"{str(number)[-1]}", end='')
        return str(number)[-1]
    except:
        print("Traceback (most recent call last):")
