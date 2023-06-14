#!/usr/bin/python3
import itertools
def roman_to_int(roman_string):
    if roman_string is None or not roman_string:
        return 0
    roman_string = roman_string.upper()
    invalid = [c for c in roman_string if c not in 'IVXLCD']
    if invalid:
        return 0
    values = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    result = 0
    for i in range(len(roman_string) - 1):
        if roman_string[i] < roman_string[i + 1]:
            result += -values[roman_string[i]]
        else:
            result += values[roman_string[i]]
    result += values[roman_string[-1]]
    return result
