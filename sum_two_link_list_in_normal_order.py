# Cracking the Coding Interview Chapter
# Sum the values of two linked lists
# list1 = 3 -> 2 -> 5
# list2 = 5 -> 2 -> 1
# Result = 8 -> 4 -> 6


class ListNode:
    def __init__(self, x):
        self.value = x
        self.next = None


_3 = ListNode(3)
_2 = ListNode(2)
_5 = ListNode(5)
_3.next = _2
_2.next = _5
list1 = _3

__5 = ListNode(5)
__2 = ListNode(2)
__1 = ListNode(1)
__5.next = __2
__2.next = __1
list2 = __5


def pad_with_zeros(list, num_of_zeros):
    current = list
    for z in range(num_of_zeros):
        zero = ListNode(0)
        zero.next = current
        current = zero
    return current


def list_len(list):
    current = list
    cnt = 0
    while current is not None:
        cnt += 1
        current = current.next
    return cnt


def sum_helper(list1, list2):
    if list1 is None and list2 is None:
        return None, 0

    prev_sum, carry = sum_helper(list1.next, list2.next)
    current_sum_val = list1.value + list2.value + carry
    if current_sum_val > 9:
        carry = 1
        current_node = ListNode(current_sum_val % 10)
    else:
        carry = 0
        current_node = ListNode(current_sum_val)

    if prev_sum is not None:
        current_node.next = prev_sum
    return current_node, carry


def sum(list1, list2):
    list1_len = list_len(list1)
    list2_len = list_len(list2)
    if list1_len > list2_len:
        list2 = pad_with_zeros(list2, list1_len - list2_len)
    elif list2_len > list1_len:
        list1 = pad_with_zeros(list1, list2_len - list1_len)
    new_head, carry = sum_helper(list1, list2)
    if carry > 0:
        head = ListNode(carry)
        head.next = new_head
        return head
    return new_head


f = ListNode(5)
r = sum(list2, f)
current = r
while current is not None:
    print(current.value)
    current = current.next
