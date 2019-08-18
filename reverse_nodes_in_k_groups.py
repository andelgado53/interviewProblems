# https://leetcode.com/problems/reverse-nodes-in-k-group/
# Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
#
# k is a positive integer and is less than or equal to the length of the linked list.
# If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.
#
# Example:
#
# Given this linked list: 1->2->3->4->5
#
# For k = 2, you should return: 2->1->4->3->5
#
# For k = 3, you should return: 3->2->1->4->5
#
# Note:
#
# Only constant extra memory is allowed.
# You may not alter the values in the list's nodes, only nodes itself may be changed.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def reverse_nodes(start_node, end_node):
    current = start_node
    previous = None

    while current is not None:
        temp = current.next
        current.next = previous
        previous = current
        current = temp
        if previous == end_node:
            # print(start_node.val)
            return previous
    
    return previous


def reverse_in_k(head, k):
    slow = head
    fast = head
    cnt = 1
    while cnt < k and fast is not None:
        fast = fast.next
        cnt += 1
    if cnt < k or fast is None:
        return head
    next = fast.next
    prev = reverse_nodes(slow, fast)
    print(prev.val)
    c = prev
    while c is not None:
        if c.next is None:
            break
        c = c.next
    c.next 
    c.next = reverse_in_k(next, k)
    return prev


_1 = ListNode(1)
_7 = ListNode(7)
_3 = ListNode(3)
_2 = ListNode(2)
__7 = ListNode(7)
_0 = ListNode(0)
__1 = ListNode(1)
__0 = ListNode(0)
___0 = ListNode(0)
_1.next = _7
_7.next = _3
_3.next = _2
_2.next = __7
__7.next = _0
_0.next = __1
__1.next = __0
__0.next = ___0

# in = [1, 7, 3, 2, 7, 0, 1, 0, 0]
# out =  [2,3,7,1,0,1,0,7,0]
h = reverse_in_k(_1, 4)
# while h is not None:
#     print(h.val)
#     h = h.next

# one = ListNode(1)
# two = ListNode(2)
# three = ListNode(3)
# four = ListNode(4)
# five = ListNode(5)
# one.next = two
# two.next = three
# three.next = four
# four.next = five

# print('*********')
# h = reverse_in_k(one, 4)
# while h is not None:
#     print(h.val)
#     h = h.next
