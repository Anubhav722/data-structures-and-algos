# Refer Problem Statement

# https://www.interviewbit.com/problems/largest-coprime-divisor/

class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer

    def _gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def cpFact(self, A, B):
        p = self._gcd(A, B)
        while p != 1:
            A /= p
            p = self._gcd(A, B)
        return A
