from itertools import permutations


class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def permute(self, A):
        x = permutations(A)
        return [list(i) for i in x]


# Crazy recursion solution.


class Solution2:
    # @param A : list of integers
    # @return a list of list of integers

    def permute(self, A):
        res = []
        left = 0
        right = len(A) - 1

        def helper(a, left, right, res):
            if left == right:
                k = a[::]
                res.append(k)
            else:
                for i in range(left, right + 1):
                    a[left], a[i] = a[i], a[left]
                    helper(a, left + 1, right, res)
                    a[left], a[i] = a[i], a[left]
        helper(A, left, right, res)
        return res
