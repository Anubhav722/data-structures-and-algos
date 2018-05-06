# https://www.interviewbit.com/problems/palindrome-partitioning/


# CRAZY RECURSION HAPPENING OVER HERE.


class Solution:
    # @param A : string
    # @return a list of list of strings
    def partition(self, A):
        ans = []
        length = len(A)

        def partitionHelper(arr, index):
            if index == length:
                ans.append(arr)
            else:
                for i in range(index, length):
                    if A[index:i + 1] == A[index:i + 1][::-1]:
                        partitionHelper(arr + [A[index:i + 1]], i + 1)

        partitionHelper([], 0)
        return ans
