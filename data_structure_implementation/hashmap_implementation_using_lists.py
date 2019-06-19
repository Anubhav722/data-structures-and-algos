### LINKS FOR THE IMPLEMENTATION:
### https://www.youtube.com/watch?v=9HFbhPscPU0&t=512s


## A hashmap is a set of key-value pairs
# i. No duplicate keys
# ii. O(1) for insert, search, delete functions
# iii. Also called dictionary, map, hash table, associative array
# iv. In python, use dict() (short for dictionary)

## Components of a Hashmap
# i. Array -> Data structure used to store the data
# ii. Hash function -> function to convert key into an array index.
# iii. Collision handling


## HASH FUNCTION WE WILL BE USING HERE.
# index = sum(ASCII value for each letter in key) % 5


class HashMap:
    def __init__(self):
        self.size = 64
        self.map = [None] * self.size

    def _get_hash(self, key):
        hash = 0
        for char in str(key):
            hash += ord(char)
        return hash % self.size

    def _insert(self, key, value):
        key_hash = self._get_hash(key)
        key_value = [key, value]

        if self.map[key_value] is None:
            self.map[key_value] = list([key_hash])
            return True
        else:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.map[key_hash].append(key_hash)
            return True

    def _search(self, key):
        key_hash = self._get_hash(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    def _delete(self, key):
        key_hash = self._get_hash(key)
        if self.map[key_hash] is None:
            return False

        for i in range(len(self.map[key_hash])):
            if self.map[key_hash][i][0] == key:
                self.map[key_hash].pop(i)
                return True

    def print(self):
        print ('---hashmap----')
        for item in self.map:
            if item:
                print (str(item))
