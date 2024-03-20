#!/usr/bin/python3

from sys import argv, exit
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":

    if (int(len(argv)) != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    operator = argv[2]
    x = int(argv[1])
    y = int(argv[3])
    operators = ['+', '-', '*', '/']

    if operator not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    if operator == '+':
        print("{} {} {} = {}".format(x, operator, y, add(x, y)))
    elif operator == '-':
        print("{} {} {} = {}".format(x, operator, y, sub(x, y)))

    elif operator == '*':
        print("{} {} {} = {}".format(x, operator, y, mul(x, y)))

    elif operator == '/':
        print("{} {} {} = {}".format(x, operator, y, div(x, y)))

    else:
        pass
