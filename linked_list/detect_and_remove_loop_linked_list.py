# Python program to detect and remove loop 

# Node class 
class Node: 

	# Constructor to initialize the node object 
	def __init__(self, data): 
		self.data = data 
		self.next = None

class LinkedList: 

	# Function to initialize head 
	def __init__(self): 
		self.head = None

	# Function to insert a new node at the beginning 
	def push(self, new_data): 
		new_node = Node(new_data) 
		new_node.next = self.head 
		self.head = new_node 

	
	def detectAndRemoveLoop(self): 

		if self.head is None : 
			return
		if self.head.next is None : 
			return

		slow = self.head 
		fast = self.head 

		# Move slow and fast 1 and 2 steps respectively 
		slow = slow.next
		fast = fast.next.next

		# Search for loop using slow and fast pointers 
		while (fast is not None): 
			if fast.next is None: 
				break
			if slow == fast : 
				break
			slow = slow.next
			fast = fast.next.next

		# if loop exists 
		if slow == fast : 
			slow = self.head 
			while (slow.next != fast.next): 
				slow = slow.next
				fast = fast.next
			
			# Sinc fast.next is the looping point 
			fast.next = None # Remove loop 


	# Utility function to print the linked LinkedList 
	def printList(self): 
		temp = self.head 
		while(temp): 
			print temp.data, 
			temp = temp.next


# Driver program 
llist = LinkedList() 
llist.head = Node(50) 
llist.head.next = Node(20) 
llist.head.next.next = Node(15) 
llist.head.next.next.next = Node(4) 
llist.head.next.next.next.next = Node(10) 

# Create a loop for testing 
llist.head.next.next.next.next.next = llist.head.next.next

llist.detectAndRemoveLoop() 

print "Linked List after removing loop"
llist.printList() 

# This code is contributed by Nikhil Kumar Singh(nickzuck_007) 

