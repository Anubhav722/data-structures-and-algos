# Rotate matrix by 90 degrees in clockwise direction.


class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def rotate(self, A):
        # transpose the matrix
        for i in range(len(A)):
            for j in range(i, len(A)):
                A[i][j], A[j][i] = A[j][i], A[i][j]
        N = len(A)
        # swap columns moving inwards from outwards
        for i in range(N / 2):
            for j in range(N):
             A[j][i], A[j][N-1-i] = A[j][N-1-i],A[j][i]
        return (A)
