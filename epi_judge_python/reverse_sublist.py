from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def reverse_sublist(L: ListNode, start: int,
                    finish: int) -> Optional[ListNode]:
    # TODO - you fill in here.
    dummy_head = sublist_head = ListNode(0, L)
    for _ in range(start - 1):
        sublist_head = sublist_head.next
    iter = sublist_head.next
    for _ in range(finish - start):
        temp = iter.next
        sublist_head.next, iter.next, temp.next = temp, temp.next, sublist_head.next
    return dummy_head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_sublist.py',
                                       'reverse_sublist.tsv', reverse_sublist))
