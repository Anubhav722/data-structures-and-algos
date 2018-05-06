from collections import Counter


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
    	n = len(A)

    	for i in range(n):
    		_sum = sum(x > A[i] for x in A)
    		if _sum == A[i]:
    			return 1
    	return -1
