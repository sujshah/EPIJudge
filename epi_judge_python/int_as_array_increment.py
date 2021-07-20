from typing import List

from test_framework import generic_test


def plus_one(A: List[int]) -> List[int]:
    # TODO - you fill in here.
    leading = 1
    for i in reversed(range(len(A))):
        A[i] += leading
        if A[i] == 10:
            A[i] = 0
            leading = 1
        else:
            leading = 0
    if leading:
        A[0] = 1
        A.append(0)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_increment.py',
                                       'int_as_array_increment.tsv', plus_one))
