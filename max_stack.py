class Stack(object):

    def __init__(self):
        """Initialize an empty stack"""
        self.items = []

    def push(self, item):
        """Push new item to stack"""
        self.items.append(item)

    def pop(self):
        """Remove and return last item"""
        # If the stack is empty, return None
        # (it would also be reasonable to throw an exception)
        if not self.items:
            return None

        return self.items.pop()

    def peek(self):
        """See what the last item is"""
        if not self.items:
            return None
        return self.items[-1]

class MaxStack:

    def __init__(self):
        self.max = Stack()
        self.items = Stack()
        self.max_item = None
    
    def push(self, item):
        if self.max_item == None:
            self.max_item = item
        elif item > self.max_item:
            self.max.push(self.max_item)
            self.max_item = item
        self.items.push(item)
    
    def pop(self):
        item = self.items.pop()
        if item == self.max_item:
            self.max_item = self.max.pop()
        return item
    
    def peek(self):
        return self.items.peek()
    
    def get_max(self):
        return self.max_item


ms = MaxStack()

ms.push(10)
print(ms.get_max())

ms.push(8)
print(ms.get_max())
# print(ms.pop())

ms.push(17)
print(ms.get_max())
ms.pop()
print(ms.get_max())

