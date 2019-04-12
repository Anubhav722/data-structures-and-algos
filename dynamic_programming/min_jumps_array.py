class Solution:

    def min_jumps_arr(self, A):
        reachable = 0
        next_reachable = 0
        jumps = 0
        last = len(A) - 1

        for i in range(len(A)):
            if reachable >= last:
                break

            if reachable < i:
                reachable = next_reachable
                jumps += 1
                if reachable < i:
                    return -1

            next_reachable = max(next_reachable, A[i] + i)

        return jumps
