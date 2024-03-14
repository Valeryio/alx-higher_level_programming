#!/usr/bin/python3

import sys
from calculator_1 import *

if (int(len(sys.argv)) != 4):
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    sys.exit(1)

operator = sys.argv[2]
x = int(sys.argv[1])
y = int(sys.argv[3])
operators = ['+', '-', '*', '/']

if operator not in operators:
    print("Unknown operator. Available operators: +, -, * and /");
    sys.exit(1)


match operator:
    case '+':
        print("{a} {op} {b} = {c}".format(a=x, op=operator, b=y, c=add(x, y)))

    case '-':
        print("{a} {op} {b} = {c}".format(a=x, op=operator, b=y, c=sub(x, y)))

    case '*':
        print("{a} {op} {b} = {c}".format(a=x, op=operator, b=y, c=mul(x, y)))

    case '/':
        print("{a} {op} {b} = {c}".format(a=x, op=operator, b=y, c=div(x, y)))

    case _:
        pass
