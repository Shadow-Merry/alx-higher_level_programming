#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx > (len(my_list) - 1) or idx < 0:
        return my_list
    else:
        new_list = list(my_list)
        new_list.index[idx] = element
        return new_list