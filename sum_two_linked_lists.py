# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example:

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.


class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


def get_node_val(node):
    if node:
        return node.val
    else:
        return 0


def sum_lists(list1, list2):
    head = ListNode(None)
    list_one_current = list1
    list_two_current = list2
    current = head
    carry = 0 
    while list_one_current or list_two_current:
        new_value = get_node_val(list_one_current) + get_node_val(list_two_current) + carry
        carry = 0
        if new_value >= 10:
            new_value = new_value % 10
            carry = 1
        new_node = ListNode(new_value)
        current.next = new_node
        current = current.next
        list_one_current = list_one_current.next if list_one_current else None
        list_two_current = list_two_current.next if list_two_current else None
    if carry > 0:
        current.next = ListNode(1)
    return head.next


list1Head = ListNode(9)
list1Head.next = ListNode(9)
list1Head.next.next = ListNode(9)

list2Head = ListNode(9)
list2Head.next = ListNode(9)
list2Head.next.next = ListNode(9)

new_list = sum_lists(list1Head, list2Head)
c = new_list
while c is not None:
    print(c.val)
    c = c.next


