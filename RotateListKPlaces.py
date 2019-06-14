# Given a linked list, rotate the list to the right by k places, where k is non-negative.

# Example 1:

# Input: 1->2->3->4->5->NULL, k = 2
# Output: 4->5->1->2->3->NULL
# Explanation:
# rotate 1 steps to the right: 5->1->2->3->4->NULL
# rotate 2 steps to the right: 4->5->1->2->3->NULL
# Example 2:

# Input: 0->1->2->NULL, k = 4
# Output: 2->0->1->NULL
# Explanation:
# rotate 1 steps to the right: 2->0->1->NULL
# rotate 2 steps to the right: 1->2->0->NULL
# rotate 3 steps to the right: 0->1->2->NULL
# rotate 4 steps to the right: 2->0->1->NULL

class LinkedListNode(object):
    def __init__(self, value):
        self.value = value
        self.next  = None


a = LinkedListNode(1)
b = LinkedListNode(2)
c = LinkedListNode(3)
d = LinkedListNode(4)
e = LinkedListNode(5)

head = a
a.next = b
b.next = c 
c.next = d
d.next = e

def rotate_list_helper(head):
    current = head
    while current.next != None:
        if current.next.next == None:
            break
        current = current.next
    new_head = current.next
    new_head.next = head
    current.next = None
    return new_head


def len_of_list(head):
    cnt = 0
    c = head
    while c != None:
        cnt +=1
        c = c.next
    return cnt


def rotate_list(head, k):
    times_to_rotate = k
    list_len = len_of_list(head)
    if k > list_len:
        times_to_rotate = k % list_len
    for r in range(times_to_rotate):
        head = rotate_list_helper(head)
    c = head
    while c != None:
        print(c.value)
        c = c.next
    

print(len_of_list(head))
print(rotate_list(head, 20000000001)) 