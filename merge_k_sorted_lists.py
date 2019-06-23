# https://leetcode.com/problems/merge-k-sorted-lists/
# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
#
# Example:
#
# Input:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# Output: 1->1->2->3->4->4->5->6


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# list one
_1 = ListNode(1)
_4 = ListNode(4)
_5 = ListNode(5)

_1.next = _4
_4.next = _5
# list 2
__1 = ListNode(1)
__3 = ListNode(3)
__4 = ListNode(4)
__1.next = __3
__3.next = __4
# List 3
___2 = ListNode(2)
___6 = ListNode(6)
___2.next = ___6
data = [_1, __1, ___2]


def merge_two_lists(list1, list2):
    dummy_head = ListNode(0)
    current1 = list1
    current2 = list2
    current_merged = dummy_head

    while current1 is not None and current2 is not None:
        if current1.val <= current2.val:
            current_merged.next = current1
            current_merged = current_merged.next
            current1 = current1.next

        else:
            current_merged.next = current2
            current_merged = current_merged.next
            current2 = current2.next

    while current1 is not None:
        current_merged.next = current1
        current_merged = current_merged.next
        current1 = current1.next

    while current2 is not None:
        current_merged.next = current2
        current_merged = current_merged.next
        current2 = current2.next
    return dummy_head.next


def merge_k_lists(lists):
    if len(lists) == 1:
        return lists[0]
    if len(lists) == 0:
        return None

    def fun(node):
        if node:
            return node.val
        else:
            return 0

    sorted(lists, key=fun)
    start_index = 1
    current = lists[0]
    while start_index < len(lists):
        current = merge_two_lists(current, lists[start_index])
        start_index += 1
    return current


h1 = merge_k_lists([_1, __1, ___2])
c = h1
while c is not None:
    print(c.val)
    c = c.next
