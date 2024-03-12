#!/usr/bin/python3

def print_last_digit(number):

    try:
        print(f"{int(number)}")
        print(f"{str(number)[-1]}", end='')
        return str(number)[-1]
    except ValueError:
        print("Traceback (most recent call last):")
