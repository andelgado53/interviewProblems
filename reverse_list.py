class LinkedListNode(object):

    def __init__(self, value):
        self.value = value
        self.next  = None

a = LinkedListNode('a')
b = LinkedListNode('b')
c = LinkedListNode('c')
d = LinkedListNode('d')
e = LinkedListNode('e')

a.next = b
b.next = c
c.next = d
d.next = e

head = a
x = head
while x:
    print(x.value)
    x = x.next


def reverse_list(head):
    current = head
    previous = None
    following = None

    while current:
        following = current.next
        current.next = previous

        previous = current
        current = following

    return previous
        


    

        
    
x = reverse_list(head)
print("***********")
while x:
    print(x.value)
    x = x.next




