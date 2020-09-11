#!/usr/bin/python3
def roman_to_int(roman_string):
    num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    if type(roman_string) != str or roman_string is None:
        return 0
    for i in range(len(roman_string)):
        if i > 0 and num[roman_string[i]] > num[roman_string[i - 1]]:
            result += num[roman_string[i]] - (num[roman_string[i - 1]] * 2)
        else:
            result += num[roman_string[i]]
    return result
