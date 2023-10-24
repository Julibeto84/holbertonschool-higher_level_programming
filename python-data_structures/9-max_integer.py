#!/usr/bin/python3
def max_integer(my_list=[]):
    max = 0
    if len(my_list) == 0:
        return None
    else:
        for element in my_list:
            if element > max:
                max = element
            return max
