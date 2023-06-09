#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    magic_counter = len(my_list)
    new_list = [None] * magic_counter

    for i in range(0, magic_counter):
        if my_list[i] % 2 == 0:
            new_list[i] = True
        else:
            new_list[i] = False
    return new_list
