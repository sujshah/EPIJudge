import functools
from typing import Optional

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def overlapping_no_cycle_lists(l0: ListNode, l1: ListNode) -> Optional[ListNode]:
    # TODO - you fill in here.
    step_0, step_1 = 0, 0
    dummy_0, dummy_1 = ListNode(0, l0), ListNode(0, l1)
    while dummy_0.next is not None:
        step_0 += 1
        dummy_0 = dummy_0.next
    while dummy_1.next is not None:
        step_1 += 1
        dummy_1 = dummy_1.next
    if dummy_0 is dummy_1:
        longer, shorter = (l1, l0) if step_1 > step_0 else (l0, l1)
        for _ in range(abs(step_1 - step_0)):
            longer = longer.next
        while longer is not shorter:
            longer, shorter = longer.next, shorter.next
        return shorter
    return None


def overlapping_no_cycle_lists_clean(l0: ListNode, l1: ListNode) -> ListNode:
    def length(L: ListNode) -> int:
        length = 0
        while L:
            length += 1
            L = L.next
        return length
    len_1, len_0 = length(l0), length(l1)
    if len_1 < len_0:
        l0, l1 = l1, l0
    for _ in range(abs(len_1 - len_0)):
        l0 = l0.next
    while l0 and l1 and l0 is not l1:
        l0, l1 = l0.next, l1.next
    return l0


@enable_executor_hook
def overlapping_no_cycle_lists_wrapper(executor, l0, l1, common):
    if common:
        if l0:
            i = l0
            while i.next:
                i = i.next
            i.next = common
        else:
            l0 = common

        if l1:
            i = l1
            while i.next:
                i = i.next
            i.next = common
        else:
            l1 = common

    result = executor.run(functools.partial(overlapping_no_cycle_lists, l0,
                                            l1))

    if result != common:
        raise TestFailure('Invalid result')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('do_terminated_lists_overlap.py',
                                       'do_terminated_lists_overlap.tsv',
                                       overlapping_no_cycle_lists_wrapper))
