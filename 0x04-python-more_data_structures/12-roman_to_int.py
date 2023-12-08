#!/usr/bin/python3
def roman_to_int(roman_string: str):
    if roman_string is None or type(roman_string) != str:
        return 0
    a = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    b = [a[x] for x in roman_string] + [0]
    c = 0

    for i in range(len(b) - 1):
        if b[i] >= b[i + 1]:
            c += b[i]
        else:
            c -= b[i]
    return c
