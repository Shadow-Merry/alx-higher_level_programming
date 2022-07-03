#!/usr/bin/python3
def element_at(my_list, idx):
    if idx > (len(my_list) - 1) or idx < 0:
        return None
    else:
        for x in my_list:
            if idx == x:
                return x
