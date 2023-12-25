#!/usr/bin/python3
def no_c(my_string):
    new_text = ""
    for char in my_string:
        if char not in ('c', 'C'):
            new_text += char
    return new_text
    