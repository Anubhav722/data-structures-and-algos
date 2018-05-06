# CRAZY SOLUTION HERE.


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def fourSum(self, A, B):
        seen = dict()

        A.sort()

        result = set()
        for i in xrange(len(A)):
            for j in xrange(i+1, len(A)):
                curr_sum = A[i] + A[j]
                diff = B - curr_sum
                if diff in seen:
                    for prev_sum in seen[diff]:
                        if A[prev_sum[1]] <= A[i] and i > prev_sum[1]:
                            result.add((A[prev_sum[0]], A[prev_sum[1]], A[i], A[j]))

                if curr_sum in seen:
                    seen[curr_sum].append((i, j))
                else:
                    seen[curr_sum] = [(i, j)]

        return sorted([list(item) for item in result])
