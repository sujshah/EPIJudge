from test_framework import generic_test

ROMAN_INTEGER_MAPPING = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}

ROMAN_INTEGER_EXCEPTIONS = {
    "I": {"V", "X"},
    "X": {"L", "C"},
    "C": {"D", "M"},
}


def roman_to_integer(s: str) -> int:
    # TODO - you fill in here.
    return roman_to_integer_standard(s) + roman_to_integer_exceptions(s)


def roman_to_integer_standard(s: str) -> int:
    return sum(ROMAN_INTEGER_MAPPING.get(x) for x in s)


def roman_to_integer_exceptions(s: str) -> int:
    total = 0
    for i in range(len(s) - 1):
        if s[i] in ROMAN_INTEGER_EXCEPTIONS and s[i + 1] in ROMAN_INTEGER_EXCEPTIONS.get(s[i]):
            total -= ROMAN_INTEGER_MAPPING.get(s[i]) * 2
    return total


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('roman_to_integer.py',
                                       'roman_to_integer.tsv',
                                       roman_to_integer))
