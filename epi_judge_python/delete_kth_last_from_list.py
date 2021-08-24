from typing import Optional

from list_node import ListNode
from test_framework import generic_test


# Assumes L has at least k nodes, deletes the k-th last node in L.
def remove_kth_last(L: ListNode, k: int) -> Optional[ListNode]:
    # TODO - you fill in here.
    kth_advanced = current = head = ListNode(0, L)
    for _ in range(k):
        kth_advanced = kth_advanced.next
    while kth_advanced.next is not None:
        current, kth_advanced = current.next, kth_advanced.next
    current.next = current.next.next
    return head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('delete_kth_last_from_list.py',
                                       'delete_kth_last_from_list.tsv',
                                       remove_kth_last))
