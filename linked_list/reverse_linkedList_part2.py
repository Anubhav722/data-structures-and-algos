
class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList(object):
    def __init__(self, head=None):
        self.head = Node(head)

    def reverseBetween(self, m, n):
        curr = self.head
        start = None
        while m > 1:
            start = curr
            curr = curr.next_node
            m -= 1
            n -= 1
        head = curr
        prev, curr = curr, curr.next_node
        while n > 1:
            tmp = curr.next_node
            curr.next_node = prev
            prev = curr
            curr = tmp
            n -= 1
        head.next_node = curr
        if start:
            start.next_node = prev
        else:
            A = prev
        return A

    def print_elements_of_linkedlist(self):
        """
        Iterative method
        """
        current_node = self.head
        while current_node:
            print current_node.data,
            current_node = current_node.get_next()

    def insert_to_beginning(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def insert_to_tail(self, data):
        new_node = Node(data)
        current_head = self.head
        while current_head.get_next() != None:
            current_head = current_head.next_node
        current_head.set_next(new_node)

    def insert_to_nth_position(self, n, data):
        new_node = Node(data)
        count = 0
        if n >= self.length():
            raise ValueError("Data cannot be inserted to random places")
        if count == n:
            temp_node = self.head
            self.head = new_node
            self.head.set_next(temp_node)
        else:
            count += 1
            current_head = self.head
            while count < n:
                count += 1
                current_head = current_head.get_next()
            temp_node = current_head.get_next()
            current_head.set_next(new_node)
            new_node.set_next(temp_node)

    def get_nth_node(self, n):
        count = 0
        if n > self.length():
            raise ValueError("n exceeds the length of the LinkedList")
        current_head = self.head
        while count < n:
            current_head = current_head.get_next()
        return current_head

    def length(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count

    def search(self, data):
        current = self.head
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        return current

    def delete(self, data):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())
