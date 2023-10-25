#!/usr/bin/python3
def max_integer(my_list=[]):
    max = my_list[0]
    if len(my_list) == 0:
        return None
    else:
        for element in range(len(my_list)):
            if my_list[element] > max:
                max = my_list[element]
        return max
