# https://www.educative.io/courses/grokking-dynamic-programming-patterns-for-coding-interviews/YQ0y0QOJQ69

def lis(A):
	return recur(A, 0, -1)

def recur(A, cur_index, prev_index):
	if cur_index == len(A):
		return 0
	c1 = 0
	if prev_index == -1 or A[cur_index] > A[prev_index]:
		return 1 + recur(A, cur_index + 1, cur_index)
	c2 = recur(A, cur_index + 1, prev_index)
	return max(c1, c2)
