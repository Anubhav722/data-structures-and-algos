# Also known as multi way tree

class TrieNode:
    def __init__(self, char):
        self.char = char
        self.children = []
	# Is it the last character of the word
	self.word_finished = False
	# how many times this character appeared in the addition process
	self.counter = 1

    
def add(root, word)
