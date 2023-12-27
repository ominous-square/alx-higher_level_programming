#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # tuple_a=[a, b]
    # tuple_b=[c,d]
    # tuple_c=[(a+c),(b+d)]
    a, b, c, d = 0
    if len(tuple_a) >= 2:
        a = tuple_a[0]
        c = tuple_a[1]
    if len(tuple_b) >= 2:
        b = tuple_b[0]
        d = tuple_b[1]
    if len(tuple_a) == 1:
        a = tuple_a[0]
    if len(tuple_b) == 1:
        b = tuple_b[0]

    tuple_c = (a + b, c + d)
    return tuple_c