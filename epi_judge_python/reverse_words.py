import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# Assume s is a list of strings, each of which is of length 1, e.g.,
# ['r', 'a', 'm', ' ', 'i', 's', ' ', 'c', 'o', 's', 't', 'l', 'y'].
def reverse_words(s: List[str]):
    # TODO - you fill in here.
    def reverse_range(start: int, finish: int) -> None:
        while start < finish:
            s[start], s[finish] = s[finish], s[start]
            start, finish = start + 1, finish - 1
    reverse_range(0, len(s) - 1)
    start = i = 0
    while i < len(s):
        while i < len(s) and s[i] != ' ':
            i += 1
        reverse_range(start, i - 1)
        start = i = i + 1
    reverse_range(start, len(s) - 1)
    return


@enable_executor_hook
def reverse_words_wrapper(executor, s):
    s_copy = list(s)

    executor.run(functools.partial(reverse_words, s_copy))

    return ''.join(s_copy)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_words.py', 'reverse_words.tsv',
                                       reverse_words_wrapper))
