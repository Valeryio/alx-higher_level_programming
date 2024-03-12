#!/usr/bin/python3

import random
number = random.randint(-10, 10)

if (number == 0):
    print(f"is zero")
elif (number > 0):
    print(f"is positive")
else:
    print(f"is negative")
