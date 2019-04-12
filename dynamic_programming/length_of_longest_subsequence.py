class Solution:

    def longestSubsequenceLength(self, A):
        m = 0
        L = [1] * len(A)

        for i in range(1, len(A)):
            for j in range(i):
                if A[j] < A[i]:
                    L[i] = max(L[i], L[j] + 1)

        R = [1] * len(A)

        for i in range(len(A) - 2, -1, -1):
            for j in range(len(A) - 1, i, -1):
                if A[j] < A[i]:
                    R[i] = max(R[i], R[j] + 1)

        for i in range(len(A)):
            val = L[i] + R[i] - 1
            m = max(m, val)
        return m
