#!/usr/bin/env python3
def uppercase(str):
    for a in str:
        ch = ord(a)
        if ch >= 97 and ch <= 122:
            ch -= 32
        print('{:c}'.format(ch), end='')
    print()
