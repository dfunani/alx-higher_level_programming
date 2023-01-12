#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return 0
    conversion = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
    r = 0
    for i, c in enumerate(roman_string):
        if c not in conversion:
            return 0
        try:
            if c == 'I' and roman_string[i + 1] in ["V", "X"]:
                r -= conversion['I']
            elif c == 'X' and roman_string[i + 1] in ["L", "C"]:
                r -= conversion['X']
            elif c == 'C' and roman_string[i + 1] in ["D", "M"]:
                r -= conversion['C']
            else:
                r += conversion[c]
        except Exception:
            r += conversion[c]
    return r
