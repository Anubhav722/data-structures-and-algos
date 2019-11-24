import requests
import json


class Node(object):
    def __init__(self, val, isWord=False):
        self.val = val
        self.children = {}
        self.isWord = isWord


class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node("")
        response = requests.get('https://api.census.gov/data/2000/surname?get=NAME,COUNT&RANK=1:100000')
        response = json.loads(response.content)
        for i in range(1, len(response)):
            string = response[i][0][::-1]
            self.insert(string)

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = Node(char)
            curr = curr.children[char]
        curr.isWord = True


    def endsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        ele = []
        prefix = prefix[::-1]
        curr = self.root
        for char in prefix:
            if char in curr.children:
                curr = curr.children[char]
            else:
                return False

        def recur(node, res, s):
            if node.isWord:
                string = prefix + s
                string = string[::-1]
                res += [string]
            if node.children:
                for key, value in node.children.items():
                    recur(value, res, s + key)

        for key, value in curr.children.items():
            res = []
            recur(value, res, key)
            ele += res
        return ele



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.endsWith(prefix)
