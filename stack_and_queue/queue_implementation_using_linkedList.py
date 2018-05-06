class Node:
    def __init__(self, value):
        self.data = value
        self.front = None

    def __repr__(self):
        return repr(self.data)


class EmptyQueueException(Exception):
    pass


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def en_queue(self, value):
        new_node = Node(value)

        if self.tail is not None:
            # make the front attribute of old node point to new node
            self.tail.front = new_node
        else:
            # if first ever node in Queue both front and tail will point to it
            self.head = new_node

        self.tail = new_node
        self.count += 1

    def de_queue(self):
        if self:
            # point head to next node
            self.head = self.head.front
            self.count -= 1
        else:
            raise EmptyQueueException()

    def peek_front(self):
        if self:
            return self.head.data
        raise EmptyQueueException()

    def peek_back(self):
        if self:
            return self.tail.data
        raise EmptyQueueException()

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.front

    def __bool__(self):
        return not (self.head is None and self.tail is None)

    def __contains__(self, value):
        return value in (node.data for node in self)

    def __len__(self):
        return self.count

    def __repr__(self):
        return 'Queue<{nodes}>'.format(nodes=', '.join(repr(node) for node in self))
