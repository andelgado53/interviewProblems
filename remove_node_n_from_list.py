# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Given a linked list, remove the n-th node from the end of list and return its head.
#
# Example:
#
# Given linked list: 1->2->3->4->5, and n = 2.
#
# After removing the second node from the end, the linked list becomes 1->2->3->5.
# Note:
#
# Given n will always be valid.
#
# Follow up:
#
# Could you do this in one pass?


class LinkedListNode(object):

    def __init__(self, value):
        self.value = value
        self.next = None


def find_parent_of_nth_from_end(head, n):
    slow = head
    fast = head
    cnt = 1
    while cnt < n:
        fast = fast.next
        cnt += 1
    while fast.next is not None:
        fast = fast.next
        if fast.next is None:
            return slow
        slow = slow.next
    return None


def remove_nth_from_end(head, n):
    parent_of_n = find_parent_of_nth_from_end(head, n)
    if parent_of_n is None:
        return head.next
    parent_of_n.next = parent_of_n.next.next
    return head


a = LinkedListNode(1)
b = LinkedListNode(2)
c = LinkedListNode(3)
d = LinkedListNode(4)
e = LinkedListNode(5)

a.next = b
b.next = c
c.next = d
d.next = e
head = a


new_head = remove_nth_from_end(a, 2)

current = new_head
while current is not None:
    print(current.value)
    current = current.next

