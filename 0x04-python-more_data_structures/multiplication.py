#!/usr/bin/python3

#Multiplication

my_list = [1, 2, 3, 4, 6]
iterable_list = [(1, 2), (3, 4), (6, 7)]


def multbynumber(my_list=[], number = 0):
    # Next... ?
    new_list = []

    for i in my_list:
        new_list.append(i * number)

    return new_list


# lambda <args> : <operation>
lambdafunc = lambda x : x * 2


# lambda x : x * 2 for i in list
# addthree = lambda x, y, z: x + y + z


#print(f"The sum of 1 + 2 + 3 = {addthree(1, 2, 3)}")
print(multbynumber(my_list, 2))

for i in my_list:
    print(lambdafunc(i),", " , end='')

# Example with map

print("That's the result with the map function : ", list(map(lambdafunc, my_list)))
print("That is the result of another test : ", list(map(lambdafunc, iterable_list)))

# map(<give_me_your_function>,  <the_list_or_iterable_you_want_use>)
