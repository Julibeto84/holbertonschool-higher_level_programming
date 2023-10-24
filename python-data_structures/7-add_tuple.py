#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuplea = tuple_a + (0, 0)
    tupleb = tuple_b + (0, 0)
    new_tuple = (tuplea[0] + tupleb[0], tuplea[1] + tupleb[1])
    return new_tuple
