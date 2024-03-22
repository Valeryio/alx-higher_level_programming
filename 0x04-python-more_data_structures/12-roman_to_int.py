#!/usr/bin/python3

def roman_to_int(roman_string):
    """
        This function returns a roman string
    Args:
        @roman_string: a roman string
    Returns:
        An integer
    """

    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    roman_exception = ['V', 'X', 'L']

    # Decomposition of the string
    roman_string = roman_string.upper();
    number_list = []
    print(roman_string)

    # Pattern matching to determine the correspond character to a string
    # character
    
    for i in roman_string:
        for key, value in roman_dict.items():
            if i == key:
                number_list.append(roman_dict[key])


    for i in range(len(number_list)):

        if number_list == 1

    # Sum of all the elements
    print(sum(number_list))

roman_to_int("x")
