# Solution:

# We define a variable minEle that stores the current min. element in the stack.
# Now the interesting part is, how to handle the case when minimum element is removed.
# To handle this, we push "2 * minEle" into the stack instead of x so that previous element
# can be retrieved using current minEle and it's value stores in stack


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return "Node {}".format(self.value)

    __repr__ = __str__


class Stack:
    def __init__(self):
        self.top = None
        self.count = 0
        self.minm = None

    def __str__(self):
        temp = self.top
        out = []
        while temp:
            out.append(str(temp.value))
            temp = temp.next

        out = '\n'.join(out)
        return "Top: {} stack: \n {}".format(self.top, out)

    __repr__ = __str__

    def getMin(self):
        if not self.top:
            return "Stack is empty"
        else:
            return self.minm

    def isEmpty(self):
        if not self.top:
            return True
        else:
            return False

    def __len__(self):
        self.count = 0
        tempNode = self.top

        while tempNode:
            tempNode = tempNode.next
            self.count += 1
        return self.count

    def peek(self):
        if not self.top:
            return -1
        else:
            if self.top.value < self.minm:
                return self.minm
            else:
                return self.top.value

    def push(self, value):
        if not self.top:
            self.top = Node(value)
            self.minm = value
        elif value < self.minm:
            temp = (value * 2) - self.minm
            new_node = Node(temp)
            new_node.next = self.top
            self.top = new_node
            self.minm = new_node
        else:
            new_node = Node(value)
            new_node.next = self.top
            self.top = new_node

    def pop(self):
        if not self.top:
            return "Stack is empty"
        else:
            removedNodeVal = self.top.value
            self.top = self.top.next
            if removedNodeVal < self.minm:
                self.minm = (self.minm * 2) - removedNodeVal
                return removedNodeVal
            else:
                return removedNodeVal
