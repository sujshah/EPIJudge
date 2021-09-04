from test_framework import generic_test

PARENTHESIS_MAPPING = {
    ")": "(",
    "}": "{",
    "]": "[",
}


def is_well_formed(s: str) -> bool:
    # TODO - you fill in here.
    stack = []
    opening = set(PARENTHESIS_MAPPING.values())
    for e in s:
        if e in opening:
            stack.append(e)
        elif not stack or PARENTHESIS_MAPPING.get(e) != stack.pop():
            return False
    return not stack


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_parenthesization.py',
                                       'is_valid_parenthesization.tsv',
                                       is_well_formed))
