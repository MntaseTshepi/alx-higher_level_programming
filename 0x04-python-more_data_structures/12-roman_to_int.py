#!/usr/bin/python3

def roman_to_int(roman_string):
    """Converts roman numeral to integer """
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_num = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
    }

    count = 0

    for i in range(len(roman_string)):

        if (i != (len(roman_string) - 1) and
                roman_num[roman_string[i]] < roman_num[roman_string[i + 1]]):
            count += roman_num[roman_string[i]] * -1
        else:
            count += roman_num[roman_string[i]]
    return (count)
