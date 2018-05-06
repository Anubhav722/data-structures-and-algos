# Problem Statement
# https://www.interviewbit.com/problems/flip/


class Solution:
    # @param A : string
    # @return a list of integers
    def flip(self, A):
        n = len(A)
        j = 1
        new_str = ''
        ans = -1
        ans_arr = []
        if A.count('1') == n:
            return []
        for i in range(1, n+1):
            if i > j:
                break
            for j in range(i, n+1):
                new_str = A[:i-1] + A[i-1:j].replace('0', '%temp%').replace('1', '0').replace('%temp%', '1') + A[j:]
                # print (new_str, i, j)
                _sum = new_str.count('1')

                if _sum > ans:
                    ans = _sum
                    ans_arr = [i,j]
        return ans_arr
