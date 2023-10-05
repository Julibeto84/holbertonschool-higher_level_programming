#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    cplist = my_list[:]
    if idx >= 0 and idx < len(my_list):
        cplist[idx] = element
    return cplist
