from math import sqrt
from typing import List

import numpy as numpy

from test_framework import generic_test


# Check if a partially filled matrix has any conflicts.
def is_valid_sudoku(partial_assignment: List[List[int]]) -> bool:
    # TODO - you fill in here.
    n = len(partial_assignment)
    if any(contains_duplicates(x) for x in partial_assignment):
        return False
    if any(contains_duplicates([partial_assignment[i][j] for i in range(n)]) for j in range(n)):
        return False
    l = int(sqrt(n))
    if any(contains_duplicates([partial_assignment[i + I][j + J] for i in range(l) for j in range(l)]) for I in
           range(0, n, l) for J in range(0, n, l)):
        return False
    return True


def contains_duplicates(block: List[int]) -> bool:
    block = list(filter(lambda x: x != 0, block))
    return len(block) != len(set(block))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_sudoku.py',
                                       'is_valid_sudoku.tsv', is_valid_sudoku))
