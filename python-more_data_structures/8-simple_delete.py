#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    for keys, value in list(a_dictionary.items()):
        if keys == key:
            del a_dictionary[key]
    return a_dictionary
