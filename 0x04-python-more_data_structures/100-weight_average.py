#!/usr/bin/python3

def weight_average(my_list=[]):
    """
        This function return weighted average
    Args:
        @my_list: the list
    Returns: A number
    """

    numerator = 0
    denominator = 0

    if len(my_list) == 0:
        return 0

    for i in range(len(my_list)):
        tmp_num = 1
        for j in range(len(my_list[i])):
            tmp_num *= (my_list[i][j])

        denominator += my_list[i][1]
        numerator += tmp_num

    return numerator / denominator
