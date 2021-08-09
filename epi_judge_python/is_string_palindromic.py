from test_framework import generic_test


def is_palindromic(s: str) -> bool:
    # TODO - you fill in here.
    i, j = 0, len(s) -1
    while i < j:
        if not s[i].isalnum():
            i += 1
            continue
        if not s[j].isalnum():
            j -= 1
            continue
        if s[i] != s[j]:
            return False
        i, j = i + 1, j - 1
    return True


if __name__ == '__main__':
    print("1")
    exit(
        generic_test.generic_test_main('is_string_palindromic.py',
                                       'is_string_palindromic.tsv',
                                       is_palindromic))
