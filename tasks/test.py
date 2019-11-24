class Node(object):
    def __init__(self, val, wordEnd=False):
        self.val = val
        self.children = {}
        self.wordEnd = False


class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node("")

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        curr = self.root
        for char in word:
            if char in curr.children:
                curr = curr.children[char]
            else:
                curr.children[char] = Node(char)
                curr = curr.children[char]
        curr.wordEnd = True
        return

    def printit(self):
        ele = []
        curr = self.root

        def recur(node, res, s):
            if node.wordEnd:
                res += [s]
            if node.children:
                for key, value in node.children.iteritems():
                    recur(value, res, s + key)

        for key, value in curr.children.iteritems():
            res = []
            recur(value, res, key)
            ele += res
        return ele
