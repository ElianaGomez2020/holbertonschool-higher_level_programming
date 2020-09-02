#!/usr/bin/python3
def print_last_digit(number):
    val = number % 10
    if number > 0:
        val = -number % 10
    print(val, end='')
    return val
