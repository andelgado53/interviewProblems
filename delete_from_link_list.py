class LinkedListNode(object):

    def __init__(self, value):
        self.value = value
        self.next  = None

class LinkedList:

    def __init__(self):
        self.head = None
    
    def add(self, node):
        if self.head == None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
    
    def iterate(self):
        node = self.head
        while node:
            print(node.value)
            node = node.next
    
    def delete1(self, node):
        node.value = self.head.value
        self.head = self.head.next

    
    def delete(self, node):
        if node.value == self.head.value:
            self.head = self.head.next
            return
        parent = self.head
        child = parent.next
        while child:
            if child.value == node.value:
                parent.next = node.next
                return
            else:
                parent = child
                child = parent.next



a = LinkedListNode('A')
b = LinkedListNode('B')
c = LinkedListNode('C')

l = LinkedList()
l.add(a)
l.add(b)
l.add(c)
l.iterate()

print("**********")
l.delete1(c)
l.iterate()
print("**********")
l.delete1(b)
l.iterate()

print("**********")
l.delete1(a)
l.iterate()
print("**********")
l.iterate()

# l.delete(b)
# # delete_node(b)
# l.iterate()
# print('head ' + l.head.value)
# print("**********")
# l.delete(a)
# print('head ' + l.head.value)
# l.iterate()
# print("**********")
# l.delete(c)
# l.iterate()

