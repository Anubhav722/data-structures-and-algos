class MidStack:

	def __init__(self):
		self.arr = []

	def push(self, item):
		return self.arr.append(item)

	def pop(self):
		return self.arr.pop()

	def isEmpty(self):
		return len(self.arr) == 0

	def findMiddle(self):
		if self.isEmpty():
			print("Stack is Empty")
			return -1
		if len(self.arr) %2 != 0:
			return self.arr[len(self.arr)/2]
		else:
			print ("There is no middle element in the stack right now")
			return -1

	def deleteMiddle(self):
		if self.isEmpty():
			print("Stack is Empty")
			return -1
		if len(self.arr) %2 != 0:
			x = self.arr[len(self.arr)/2]
			del self.arr[len(self.arr)/2]
			return x
		else:
			print ("There is no middle element in the stack right now")
			return -1