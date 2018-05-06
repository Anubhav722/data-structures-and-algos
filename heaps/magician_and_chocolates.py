# REFERENCE LINK: https://www.interviewbit.com/problems/magician-and-chocolates/

import heapq


class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return an integer
    def nchoc(self, A, B):
        heap = []
        for x in B:
            # FOLLOWING MAX HEAP CONCEPT.
            # MAX. ELEMENT WILL BE OMITTED FROM THE HEAP.
            # SINCE THEY ALL ARE CHANGED TO NEGATIVE.
            heapq.heappush(heap, -x)

        count = 0
        for i in range(A):
            val = heapq.heappop(heap)
            count += (-val)
            heapq.heappush(heap, -((-val)/2))
        return count % (10**9 + 7)
