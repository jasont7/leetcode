class Node:
    def __init__(self, val=None, minval=None, nextnode=None):
        self.val = val
        self.min = minval
        self.next = nextnode

class MinStack(object):
    def __init__(self):
        self.head = None

    def push(self, val):
        if not self.head:
            self.head = Node(val, val, None)
        else:
            self.head = Node(val, min(val, self.head.min), self.head)

    def pop(self):
        self.head = self.head.next
        
    def top(self):
        return self.head.val

    def getMin(self):
        return self.head.min
