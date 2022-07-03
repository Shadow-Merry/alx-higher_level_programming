#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = list(my_list)
    for x in my_list:
        if x == 0:
            new_list[x] = True
        elif (x % 2) != 0:
            new_list[x] = False
        else:
            new_list[x] = True
    return new_list
