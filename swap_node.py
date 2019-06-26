# https://leetcode.com/problems/swap-nodes-in-pairs/
# Given a linked list, swap every two adjacent nodes and return its head.
# You may not modify the values in the list 's nodes, only nodes itself may be changed.
#
# Example:
#
# Given
# 1->2->3->4, you
# should
# return the
# list as 2->1->4->3.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def swap_pair(head):
    current = head
    new_head = head
    if current and current.next:
        following = current.next
        temp = following.next
        following.next = current
        new_head = following
        current.next = temp
        previous = current
        current = temp
    else:
        return new_head

    while current is not None and current.next is not None:
        following = current.next
        temp = following.next
        following.next = current
        previous.next = following
        current.next = temp
        previous = current
        current = temp
    return new_head


one = ListNode(1)
two = ListNode(2)
three = ListNode(3)
four = ListNode(4)
five = ListNode(5)
one.next = two
two.next = three
three.next = four
four.next = five

c1 = one
while c1 is not None:
    print(c1.val)
    c1 = c1.next

print("***********")
new_head = swap_pair(one)

c = new_head
while c is not None:
    print(c.val)
    c = c.next