class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def diagonal(self, A):
        n = len(A)
        r = []
        for i in range(n):
            b = []
            for j in range(i+1):
                b.append(A[j][i-j])

            r.append(b)

        for i in range(1,n):
            b = []
            for j in range(n-1, i-1, -1):
                b.append(A[i+(n-1-j)][j])

            r.append(b)

        return r
