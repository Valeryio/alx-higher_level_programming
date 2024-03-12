#!/usr/bin/python3

def print_last_digit(number):

    try:
        numberVerificator = int(number)
    except ValueError:
        return

    print(f"{str(number)[-1]}", end='')
    return str(number)[-1]
