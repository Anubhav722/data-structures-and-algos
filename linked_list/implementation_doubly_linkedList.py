class Node(object):

    def __init__(self, data=None, next_node=None, prev_node=None):
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def get_prev(self):
        return self.prev_node

    def set_next(self, new_next):
        self.next_node = new_next

    def set_prev(self, new_prev):
        self.prev_node = new_prev


class LinkedList(object):
    def __init__(self, head=None):
        self.head = Node(head)

    def insert_to_beginning(self, data):
        new_node = Node(data)
        current_head = self.head
        current_head.prev_node = new_node
        new_node.set_next(self.head)
        self.head = new_node

    def insert_to_tail(self, data):
        new_node = Node(data)
        current_head = self.head
        while current_head.get_next():
            current_head = current_head.next_node
        current_head.set_next(new_node)
        new_node.set_prev(current_head)
