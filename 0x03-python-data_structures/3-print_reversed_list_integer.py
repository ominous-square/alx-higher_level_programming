#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return
    my_new_list=my_list[::-1]
    print (my_new_list)