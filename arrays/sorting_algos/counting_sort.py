# Counting sort is the lower bound algorithm for sorting
# It's time complexity is theta(n).
# This algorithm is only used to sort positive integers


def counting_sort(A):
	max_el = max(A)
	result_arr = [0 for i in range(max_el+1)]
	ans = []
	for i in range(len(A)):
		result_arr[A[i]] += 1

	for i in range(len(result_arr)):
		if result_arr[i]:
			ans.extend([i]*result_arr[i])
	return ans

print (counting_sort([3,7,9,2,3,2,1,9]))