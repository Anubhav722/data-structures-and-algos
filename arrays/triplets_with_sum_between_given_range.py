class Solution:
    # @param A : list of strings
    # @return an integer
    def solve(self, A):
        res = [float(A[0]), float(A[1])] 

        for i in range(2, len(A)):
            res.append(float(A[i]))
            if sum(res) < 1:
                res.remove(min(res))
                continue
            if sum(res) > 2:
                res.remove(max(res))
                continue
            if sum(res) >1 and sum(res) < 2:
                return 1 
        return 0