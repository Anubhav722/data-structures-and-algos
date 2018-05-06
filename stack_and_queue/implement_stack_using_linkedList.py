class Node(object):

    def __init__(self, data):
        self.data = data
        self.next_node = None


class Stack(object):

    def __init__(self):
        self.root = None

    def isEmpty(self):
        return True if self.root is None else False

    def push(self, data):
        new_node = Node(data)
        new_node.next_node = self.root
        self.root = new_node

    def pop(self):
        if self.isEmpty():
            return float("-inf")
        temp = self.root
        self.root = self.root.next
        popped = temp.data
        return popped

    def peek(self):
        if self.isEmpty():
            return float("-inf")
        return self.root.data
