#!/usr/bin/python3

import random
number = random.randint(-10000, 10000)
numberStr = str(number)
if (int(numberStr[-1]) > 5 and number > 0):
    print(f"Last digit of {number} \
is {int(numberStr[-1])} and is greater than 5")

if (int(numberStr[-1]) == 0):
    print(f"Last digit of {number} is {int(numberStr[-1])} and is 0")

elif (int(numberStr[-1]) < 6 or number < 0):
    print(f"Last digit of {number} is \
{int(numberStr[-1])} and is less than 6 and not 0")
else:
    pass
