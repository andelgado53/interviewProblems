# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Example:
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.


class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


def print_link_list(node):
    current = node
    while current is not None:
        print(current.value)
        current = current.next


list1 = ListNode(3)
three = ListNode(9)
four = ListNode(9)
three.next = four
list1.next = three

list2 = ListNode(9)
one = ListNode(9)
list2.next = one
two = ListNode(9)
one.next = two


def get_value(node):
    if node and node.value:
        return node.value
    else:
        return 0


def sum(list1, list2):
    dummy_head = ListNode(None)
    result = dummy_head
    current1 = list1
    current2 = list2
    carry = 0

    while current1 or current2:
        value = get_value(current1) + get_value(current2) + carry
        carry = 0
        if value > 9:
            carry = 1
            value = value % 10
        new_node = ListNode(value)
        result.next = new_node
        current1 = current1.next if current1 else None
        current2 = current2.next if current2 else None
        result = result.next
    if carry > 0:
        result.next = ListNode(carry)
    return dummy_head.next


print_link_list(sum(list1, list2))
