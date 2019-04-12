from collections import defaultdict


class Solution:

    def solve(self, A):
        n = len(A)

        if not n:
            return 0
        if n == 1:
            return 1

        dp = defaultdict(int)

        for i in range(1, len(A)):
            for j in range(i):
                diff = abs(A[i] - A[j])
                dp[(i, diff)] = max(dp[(i, diff)], dp[(j, diff)])

        return max(dp.values()) + 1
