class Solution:

    def numDecodings(self, A):
        dp = [0] * (len(A) + 1)
        dp[0] = 1

        for i in range(len(dp)):
            if A[i - 1] != '0':
                dp[i] = dp[i - 1]

            if i != 1 and '10' <= A[i - 2:i] <= '26':
                dp[i] += dp[i - 2]

        return dp[-1]
