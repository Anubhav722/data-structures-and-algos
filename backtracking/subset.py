class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def subsets(self, A):
        A.sort()
        r = [[]]
        for e in A:
            r += [x + [e] for x in r]
        return sorted(r)
