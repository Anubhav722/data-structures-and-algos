def createstack():
	stack = []
	return stack

def push(stack, item):
	return stack.append(item)

def isEmpty(stack):
	return len(stack) == 0

def pop(stack):
	if isEmpty(stack):
		return "UnderFlow"
	return stack.pop()

def peek(stack):
	if isEmpty(stack):
		return "UnderFlow"
	return stack[-1]