# FIND THE MAXIMUM SUM AND SUB ARRAY WHICH GIVES THE MAXIMUM SUM.

# Refer this video to get more comfortable.
# https://www.youtube.com/watch?v=ohHWQf1HDfU&feature=player_embedded

import sys


# Kadane's Algorithm
# Time complexity is O(n)
def Maximum_Sub_Array(arr, n):
    ans = 0
    _sum = 0
    num_of_neg_values = 0
    for i in range(n):
        if arr[i] < 0:
            num_of_neg_values += 1
        if (_sum + arr[i] > 0):
            _sum += arr[i]
        else:
            _sum = 0
        ans = max(_sum, ans)
        if num_of_neg_values == n:
            return max(arr)
    return ans


# Divide and Conquer algorithm
# Time complexity is O(nlogn)


def Max_Sub_Array(arr, n):

    # Handling base case if len(arr) == 1
    if (n == 1):
        return arr[0]
    m = n / 2
    left_mss = Max_Sub_Array(arr, m)
    right_mss = Max_Sub_Array(arr[m:], n - m)

    left_sum = - sys.maxint - 1
    right_sum = -sys.maxint - 1
    _sum = 0

    for i in range(m, n):
        _sum += arr[i]
        right_sum = max(right_sum, _sum)

    _sum = 0
    for i in range(m - 1, -1, -1):
        _sum += arr[i]
        left_sum = max(left_sum, _sum)

    ans = max(left_mss, right_mss)
    return max(ans, left_sum + right_sum)



# Another brute force algorithm
# Solving this question using the last sum of the sub array
# Overall time complexity is O(n^2)

def maximum_sub_array(arr, n):
    ans = - sys.maxint - 1
    for start_index in range(0, n):
        _sum = 0
        for sub_array_size in range(1,n+1):

            if (start_index + sub_array_size > n): # Subarray exceeds array bounds
                break

            _sum += arr[start_index + sub_array_size -1] # Last element of the new Subarray
            ans = max(ans, _sum)

    return ans



# Solving this question using brute force here.
# Overall time complexity of this function is O(n^3).


def max_sub_array(arr, n):
    ans = - sys.maxint - 1

    for sub_array_size in range(1, n+1):
        for start_index in range(n):

            if (start_index + sub_array_size > n):
                break
            _sum = 0

            for i in range(start_index, start_index+sub_array_size):
                _sum += arr[i]
            ans = max(ans, _sum)

    return ans
