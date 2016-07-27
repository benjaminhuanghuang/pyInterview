'''
13. Roman to Integer

Given a roman numeral, convert it to an integer.
Example
    IV -> 4
    XII -> 12
    XXI -> 21
    XCIX -> 99

Input is guaranteed to be within the range from 1 to 3999.

'''


def roman_to_int(s):
    ROMAN = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    if s == "":
        return 0

    index = len(s) - 2
    sum = ROMAN[s[-1]]
    while index >= 0:
        if ROMAN[s[index]] < ROMAN[s[index + 1]]:
            sum -= ROMAN[s[index]]
        else:
            sum += ROMAN[s[index]]
        index -= 1
    return sum
