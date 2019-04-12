class Solution:

    def canJump(self, A):
        farthest = 0

        for i in range(len(A) - 1):
            farthest = max(farthest, A[i] + i)

            if farthest == i:
                return 0

        return 1
