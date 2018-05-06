# Problem Statement:
# https://www.interviewbit.com/problems/square-root-of-integer/


# SOlving this problem statement using binary search.


class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):
        if A == 0 or A == 1:
            return A
        low = 2
        high = A / 2
        # mid = low + (high - low) / 2
        while low <= high:
            # To avoid overflow mid is being calculated like this.
            # REMEMBER: 32 bit signed integer.
            mid = low + (high - low) / 2
            if mid * mid == A:
                return mid
            elif mid * mid > A:
                high = mid - 1
            else:
                low = mid + 1
        if mid * mid > A:
            mid = mid - 1
        return mid


# A pythonic approach

# import math


# class Solution:
#     # @param A : integer
#     # @return an integer
#     def sqrt(self, A):
#         return int(math.floor(A**.5))
