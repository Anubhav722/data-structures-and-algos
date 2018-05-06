class Solution:
    # @param A : integer
    # @return a boolean
    def isPower(self, A):
        if A == 1:
            return True
        p = 2

        while 2 ** p <= A:
            pthRoot = round(A ** (1.0 / p), 8)
            if int(pthRoot) == pthRoot:
                return True
            p += 1
        return False
