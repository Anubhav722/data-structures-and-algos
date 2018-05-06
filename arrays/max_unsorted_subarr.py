class Solution:
    # @param A : list of integers
    # @return a list of integers
    def subUnsort(self, A):
        mirror_A = sorted(A)

        arr_index = []
        if A == mirror_A:
            return [-1]
        n = len(A)
        for i in range(n):
            if A[i] != mirror_A[i]:
                if len(arr_index) == 0:
                    arr_index.append(i)
                else:
                    arr_index.append(i)

        return [arr_index[0], arr_index[-1]]
