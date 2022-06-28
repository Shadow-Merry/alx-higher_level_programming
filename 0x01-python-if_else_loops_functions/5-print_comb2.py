#!/usr/bin/python3
for x in range(100):
    if x < 10:
        print(f"0{x}", end=", ")
    elif x == 99:
        print(x)
    else:
        print(f"{x}", end=", ")
