from test_framework import generic_test


def reverse(x: int) -> int:
    # TODO - you fill in here.
    result, remaining_x = 0, abs(x)
    while remaining_x:
        result = result * 10 + remaining_x % 10
        remaining_x //= 10
    return -result if x < 0 else result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_digits.py',
                                       'reverse_digits.tsv', reverse))
