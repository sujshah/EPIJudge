from test_framework import generic_test


def evaluate(expression: str) -> int:
    # TODO - you fill in here.
    elements = expression.split(",")
    stack = []
    for e in elements:
        if e.isnumeric():
            stack.append(int(e))
        else:
            b, a = int(stack.pop()), int(stack.pop())
            if e == "+":
                stack.append(a + b)
            elif e == "/":
                stack.append(a // b)
            elif e == "*":
                stack.append(a * b)
            elif e == "-":
                stack.append(a - b)
    return int(stack.pop())


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('evaluate_rpn.py', 'evaluate_rpn.tsv',
                                       evaluate))
