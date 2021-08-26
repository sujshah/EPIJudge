from list_node import ListNode
from test_framework import generic_test


def is_linked_list_a_palindrome(L: ListNode) -> bool:
    # TODO - you fill in here.
    if not L: return True

    def length(head: ListNode) -> int:
        # can use slow, fast pointers to remove this!
        counter = 0
        while head:
            head = head.next
            counter += 1
        return counter

    n = length(L)
    head = tail = L
    for _ in range(n // 2):
        tail = tail.next
    following = tail.next
    for _ in range(n // 2, n - 1):
        following.next, tail, following = tail, following, following.next
    for _ in range(n // 2):
        if tail.data != head.data:
            return False
        tail, head = tail.next, head.next
    return True


if __name__ == '__main__':
    a = ListNode(0)
    a.next = ListNode(1)
    a.next.next = ListNode(3)
    a.next.next.next = ListNode(3)
    a.next.next.next.next = ListNode(1)
    a.next.next.next.next.next = ListNode(0)
    exit(
        generic_test.generic_test_main('is_list_palindromic.py',
                                       'is_list_palindromic.tsv',
                                       is_linked_list_a_palindrome))
