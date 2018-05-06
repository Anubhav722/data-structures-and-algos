# Absolutely didn't get the logic.


class Solution:

    def isPaintableIn(self, painters, T, Boards, Time):
        p = 0
        for i in xrange(painters):
            total = 0
            while p < len(Boards) and total + Boards[p] * T <= Time:
                total += Boards[p] * T
                p += 1
        return p == len(Boards)
    # @param A : integer
    # @param B : integer
    # @param C : list of integers
    # @return an integer

    def paint(self, A, B, C):
        maxTime = 1
        while not self.isPaintableIn(A, B, C, maxTime):
            maxTime *= 2
        left = maxTime / 2
        right = maxTime
        while left < right:
            mid = left + (right - left) / 2
            if self.isPaintableIn(A, B, C, mid):
                right = mid
            else:
                left = mid + 1
        return left % 10000003
