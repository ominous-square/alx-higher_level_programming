#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    my_copy_list = my_list.copy()
    if idx < 0 or idx >= len(my_list):
        return my_copy_list
    my_copy_list [idx] = element
    return my_copy_list