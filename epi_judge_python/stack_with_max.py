import collections
from dataclasses import dataclass, field
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure

StackWithMax = collections.namedtuple("StackWithMax", ("element", "max"))


@dataclass
class Stack:
    stack: List[StackWithMax] = field(default_factory=list)

    def empty(self) -> bool:
        # TODO - you fill in here.
        return len(self.stack) == 0

    def max(self) -> int:
        # TODO - you fill in here.
        return self.stack[-1].max

    def pop(self) -> int:
        # TODO - you fill in here.
        return self.stack.pop().element

    def push(self, x: int) -> None:
        # TODO - you fill in here.
        self.stack.append(StackWithMax(x, x) if self.empty() else StackWithMax(x, max(x, self.max())))


def stack_tester(ops):
    try:
        s = Stack()

        for (op, arg) in ops:
            if op == 'Stack':
                s = Stack()
            elif op == 'push':
                s.push(arg)
            elif op == 'pop':
                result = s.pop()
                if result != arg:
                    raise TestFailure('Pop: expected ' + str(arg) + ', got ' +
                                      str(result))
            elif op == 'max':
                result = s.max()
                if result != arg:
                    raise TestFailure('Max: expected ' + str(arg) + ', got ' +
                                      str(result))
            elif op == 'empty':
                result = int(s.empty())
                if result != arg:
                    raise TestFailure('Empty: expected ' + str(arg) +
                                      ', got ' + str(result))
            else:
                raise RuntimeError('Unsupported stack operation: ' + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('stack_with_max.py',
                                       'stack_with_max.tsv', stack_tester))
