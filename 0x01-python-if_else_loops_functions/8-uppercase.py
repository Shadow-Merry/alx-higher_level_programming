#!/usr/bin/python3
def uppercase(str):
    for x in str:
        if x > 96 and x < 123:
            x = x - 32
        print("{:c}".format(x), end=' ')
    print()
