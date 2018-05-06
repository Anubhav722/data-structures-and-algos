# Important question.
# https://www.interviewbit.com/problems/combinations/


# Crazy recursion function implementation.


class Solution:
    # @param n : integer
    # @param k : integer
    # @return a list of list of integers
    def combine(self, n, k):

        if k > n:
            return []

        ans = []
        arr = range(1, n + 1)

        def combineHelper(k, i, res):
            if k == 0:
                ans.append(res)
            else:
                for j in range(i + 1, len(arr)):
                    combineHelper(k - 1, j, res + [arr[j]])

        combineHelper(k, -1, [])
        return ans


# USING PYTHON'S BUILT IN LIBRARY.
# import itertools


# class Solution:
#     # @param A : integer
#     # @param B : integer
#     # @return a list of list of integers
#     def combine(self, A, B):
#         x = range(1, A + 1)
#         y = itertools.combinations(x, B)
#         return [list(i) for i in y]
