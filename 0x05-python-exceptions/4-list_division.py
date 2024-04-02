#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new_list = []

    for i in range(0, list_length):
        try:
            c = float(my_list_1[i]) / float(my_list_2[i])
        except ValueError:
            c = 0
            print("wrong type")
        except IndexError:
            c = 0
            print("out of range")
        except ZeroDivisionError:
            c = 0
            print("division by 0")
        finally:
            new_list.append(c)
    return new_list
