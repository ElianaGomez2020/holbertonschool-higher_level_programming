#!/usr/bin/python3
for a in range(122, 96, -1):
    print(("{:c}".format(a) if a % 2 == 0 else "{:c}".format(a - 32)), end="")
