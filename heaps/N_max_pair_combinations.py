from heapq import heappush, heappop


class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def solve(self, A, B):
        n = len(A)
        A.sort()
        A.reverse()
        B.sort()
        B.reverse()

        h = []
        for x in A:
            for y in B:
                v = x + y
                if len(h) < n:
                    heappush(h, v)
                else:
                    if h[0] < v:
                        heappop(h)
                        heappush(h, v)
                    else:
                        break
        h.sort()
        h.reverse()
        return h
