from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def even_odd_merge(L: ListNode) -> Optional[ListNode]:
    # TODO: Clean up - solved wrong problem in first instance!
    if L is None:
        return None
    last_even, first_odd, last_odd = L, None, None
    pointer = L.next
    turn = 1
    while pointer is not None:
        last_node = last_even if not turn else last_odd
        if not turn:
            last_even.next = pointer
            last_even, last_even.next, pointer = last_even.next, None, pointer.next
        elif not last_node:
            last_odd, last_odd.next, first_odd, pointer = pointer, None, pointer, pointer.next
        else:
            last_odd.next = pointer
            last_odd, last_odd.next, pointer = last_odd.next, None, pointer.next
        turn ^= 1
    last_even.next = first_odd
    return L


if __name__ == '__main__':
    a = ListNode(0)
    a.next = ListNode(1)
    a.next.next = ListNode(2)
    a.next.next.next = ListNode(3)
    a.next.next.next.next = ListNode(4)
    a.next.next.next.next.next = ListNode(5)
    a.next.next.next.next.next.next = ListNode(7)
    print(even_odd_merge(a))
    # quit()

    exit(
        generic_test.generic_test_main('even_odd_list_merge.py',
                                       'even_odd_list_merge.tsv',
                                       even_odd_merge))
