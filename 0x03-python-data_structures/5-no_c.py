#!/usr/bin/python3
def no_c(my_string):
    count = 0
    new_list = list(my_string)
    for x in my_string:
        if x == 'c' or x == 'C':
            new_list[count] = ""
        count += 1
    return "".join(new_list)
