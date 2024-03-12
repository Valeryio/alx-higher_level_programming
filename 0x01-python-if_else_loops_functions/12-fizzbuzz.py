#!/usr/bin/python3

def fizzbuzz():

    for i in range(1, 101):
        if (isMultipleThree(i) and isMultipleFive(i)):
            print("FizzBuzz", end=' ')
        elif (isMultipleThree(i)):
            print("Fizz", end=' ')
        elif (isMultipleFive(i)):
            print("Buzz", end=' ')
        else:
            print("{n}".format(n=i), end=' ')


def isMultipleThree(x):

    if (x % 3 == 0):
        return True


def isMultipleFive(x):

    if (x % 5 == 0):
        return True
    return False
