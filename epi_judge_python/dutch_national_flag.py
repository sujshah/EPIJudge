import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

RED, WHITE, BLUE = range(3)


def dutch_flag_partition(pivot_index: int, A: List[int]) -> None:
    # TODO - you fill in here.
    counter = 0
    pivot_value = A[pivot_index]
    for i in range(len(A)):
        if A[i] < pivot_value:
            A[counter], A[i] = A[i], A[counter]
            counter += 1
    counter = len(A) - 1
    for i in reversed(range(len(A))):
        if A[i] > pivot_value:
            A[counter], A[i] = A[i], A[counter]
            counter -= 1
    return


def dutch_flag_partition_alternative(pivot_index: int, A: List[int]) -> None:
    pivot_value = A[pivot_index]
    smallest, equal, largest = 0, 0, len(A)
    while equal < largest:
        value = A[equal]
        if value < pivot_value:
            A[equal], A[smallest] = A[smallest], A[equal]
            smallest += 1
            equal += 1
        elif value == pivot_value:
            equal += 1
        else:
            A[equal], A[largest - 1] = A[largest - 1], A[equal]
            largest -= 1


@enable_executor_hook
def dutch_flag_partition_wrapper(executor, A, pivot_idx):
    count = [0, 0, 0]
    for x in A:
        count[x] += 1
    pivot = A[pivot_idx]

    executor.run(functools.partial(dutch_flag_partition_alternative, pivot_idx, A))

    i = 0
    while i < len(A) and A[i] < pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] == pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] > pivot:
        count[A[i]] -= 1
        i += 1

    if i != len(A):
        raise TestFailure('Not partitioned after {}th element'.format(i))
    elif any(count):
        raise TestFailure('Some elements are missing from original array')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('dutch_national_flag.py',
                                       'dutch_national_flag.tsv',
                                       dutch_flag_partition_wrapper))
