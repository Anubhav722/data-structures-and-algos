# https://leetcode.com/problems/string-compression/

class Solution(object):

    def compress(self, A):
        n = len(A)
        res = ''
        count = 1
        for i in range(1, n):
            if A[i] == A[i-1]:
                count += 1
            else:
                res += A[i-1] + str(count)
                count = 1
        res += str(count) + A[-1]
        return res
