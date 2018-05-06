# Suppose a sorted array is rotated at some pivot unknown to you beforehand.

# (i.e., 0 1 2 4 5 6 7  might become 4 5 6 7 0 1 2 ).

# You are given a target value to search. If found in the array, return its index, otherwise return -1.

# You may assume no duplicate exists in the array.

# Input : [4 5 6 7 0 1 2] and target = 4
# Output : 0


class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def search(self, A, B):

        lft, rgt = 0, len(A)-1
        while lft<=rgt:
            mid = (lft+rgt)/2
            l, m, r = A[lft], A[mid], A[rgt]
            if m == B:
                return mid
            elif l <= B < m or (l > m and not(m < B <= r)):
                # We choose left half if either : 
                #    * left half is sorted and B in this range
                #    * left half is not sorted, 
                #      but B isn't in the sorted right half.
                rgt = mid-1
            else:
                lft = mid+1

        return -1
