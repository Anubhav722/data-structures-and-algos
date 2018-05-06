class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def diffPossible(self, A, B):
        complements = set()
        for a in A:
            if a - B in complements or a + B in complements:
                return 1
            complements.add(a)

        return 0
