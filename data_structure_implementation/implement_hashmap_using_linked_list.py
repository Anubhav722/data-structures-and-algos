class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.next = None
        self.prev = None


class HashMap:
    def __init__(self, capacity):
        self.capacity = capacity
        self.head = None
    
    def get_hash(self, key):
        return key % self.capacity

    def put(self, key, value):
        index = self.get_hash(key)
        
