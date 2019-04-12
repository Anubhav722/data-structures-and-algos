class Solution:

    def climbStairs(self, A):
        dp = [0] * len(A)

        if A == 1:
            return 1

        dp[0] = 1
        dp[1] = 2

        for i in range(2, A):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[-1]
