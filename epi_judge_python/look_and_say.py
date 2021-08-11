from test_framework import generic_test


def look_and_say(n: int) -> str:
    # TODO - you fill in here.
    s = "1"
    for _ in range(n - 1):
        s = look_and_say_iteration(s)
    return s


def look_and_say_iteration(s: str) -> str:
    start, counter, result = 0, 0, []
    while counter < len(s):
        while counter < len(s) and s[start] == s[counter]:
            counter += 1
        result.extend([str(counter - start), s[start]])
        start = counter
    return "".join(result)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('look_and_say.py', 'look_and_say.tsv',
                                       look_and_say))
