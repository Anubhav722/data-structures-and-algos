# Returns the maximum length
# Preffered and EASY to UNDERSTAND solution.


def maxLen2(arr):

    # NOTE: Dictonary in python in implemented as Hash Maps
    # Create an empty hash map (dictionary)
    hash_map = {}

    # Initialize result
    max_len = 0
    temp_max_len = 0
    max_arr = []

    # Initialize sum of elements
    curr_sum = 0
    # import ipdb; ipdb.set_trace()
    # Traverse through the given array
    for i in range(len(arr)):

        # Add the current element to the sum
        curr_sum += arr[i]

        if arr[i] is 0 and max_len is 0:
            max_len = 1

        if curr_sum is 0:
            max_len = i + 1

        # NOTE: 'in' operation in dictionary to search
        # key takes O(1). Look if current sum is seen
        # before
        if curr_sum in hash_map:
            temp_max_len = max_len
            max_len = max(max_len, i - hash_map[curr_sum])
            if temp_max_len != max_len:
                max_arr = arr[hash_map[curr_sum]+1: i+1]
        else:

            # else put this sum in dictionary
            hash_map[curr_sum] = i

    return max_arr


# Python program to find the length of largest subarray with 0 sum
# returns the length
# Time Complexity is O(n^2)
# Not the best solution.


def maxLen(arr):

    # initialize result
    max_len = 0
    max_arr = []
    temp_max_len = 0

    # pick a starting point
    for i in range(len(arr)):

        # initialize sum for every starting point
        curr_sum = 0

        # try all subarrays starting with 'i'
        for j in range(i, len(arr)):

            curr_sum += arr[j]

            # if curr_sum becomes 0, then update max_len
            if curr_sum == 0:
                temp_max_len = max_len
                max_len = max(max_len, j - i + 1)
                if max_len != temp_max_len:
                    max_arr = arr[i:j + 1]
    return max_arr


# Solution as per interviewbit.
# A bot complex solution.


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def lszero(self, A):
        seen_sums = dict()
        sm = 0
        strt, end = 0, 0
        seen_sums[0] = 0
        for index, value in enumerate(A, 1):
            sm += value
            if sm in seen_sums:
                if end - strt < index - seen_sums[sm]:
                    strt, end = seen_sums[sm], index
            else:
                seen_sums[sm] = index

        return A[strt:end] if strt != end else []
