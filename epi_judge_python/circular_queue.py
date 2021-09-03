from test_framework import generic_test
from test_framework.test_failure import TestFailure


class Queue:
    SCALING_FACTOR = 2

    def __init__(self, capacity: int) -> None:
        # TODO - you fill in here.
        self.queue = [0] * capacity
        self.head = self.tail = self.num = 0

    def enqueue(self, x: int) -> None:
        # TODO - you fill in here.
        if len(self.queue) == self.num:
            self.queue = self.queue[self.head:] + self.queue[:self.head]
            self.head, self.tail = 0, self.num
            self.queue = self.queue + [0] * len(self.queue)
        self.queue[self.tail] = x
        self.tail = (self.tail + 1) % len(self.queue)
        self.num += 1

    def dequeue(self) -> int:
        # TODO - you fill in here.
        value = self.queue[self.head]
        self.head, self.num = (self.head + 1) % len(self.queue), self.num - 1
        return value

    def size(self) -> int:
        # TODO - you fill in here.
        return self.num


def queue_tester(ops):
    q = Queue(1)

    for (op, arg) in ops:
        if op == 'Queue':
            q = Queue(arg)
        elif op == 'enqueue':
            q.enqueue(arg)
        elif op == 'dequeue':
            result = q.dequeue()
            if result != arg:
                raise TestFailure('Dequeue: expected ' + str(arg) + ', got ' +
                                  str(result))
        elif op == 'size':
            result = q.size()
            if result != arg:
                raise TestFailure('Size: expected ' + str(arg) + ', got ' +
                                  str(result))
        else:
            raise RuntimeError('Unsupported queue operation: ' + op)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('circular_queue.py',
                                       'circular_queue.tsv', queue_tester))
