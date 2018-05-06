# This one times out.
# https://www.interviewbit.com/problems/kth-permutation-sequence/


import itertools


class Solution:
    # @param A : integer
    # @param B : integer
    # @return a strings
    def getPermutation(self, A, B):
        x = itertools.permutations(range(1, A+1))
        y = [list(i) for i in x]
        return "".join(str(i) for i in y[B-1])


class Solution2:
    # @param n : integer
    # @param k : integer
    # @return a strings
    def getPermutation(self, n, k):

        arr = range(1, n + 1)
        res = []

        def factorial(num):
            fact = 1
            for i in range(1, num + 1):
                fact = fact * i
            return fact

        def helper(soFar, arr, count, factIndex):

            if len(arr) == 0:
                if count[0] + 1 == k:
                    res.append(soFar)
                    return True
                else:
                    count[0] += 1
            else:
                for i in range(len(arr)):
                    fact = factorial(factIndex)
                    if fact + count[0] >= k:
                        if helper(soFar + str(arr[i]) , arr[:i] + arr[i+1:] , count , factIndex-1):
                            return True
                    else:
                        count[0] += fact

                return False

        if helper('', arr, [0], n - 1):
            return res[0]
        else:
            return ''
