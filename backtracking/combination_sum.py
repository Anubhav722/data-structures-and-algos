# https://www.interviewbit.com/problems/combination-sum/


class Solution2:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        candidates.sort()
        res = []
        self.DFS(candidates, target, 0, res, [])
        return res

    def DFS(self, candidates, target, start, res, intermedia):
        if target == 0:
            res.append(intermedia)
            return
        for i in range(start, len(candidates)):
            if target < candidates[i]:
                return
            self.DFS(candidates,target - candidates[i], i, res, intermedia + [candidates[i]])

# Crazy recursion solution.


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def combSum(self, A, B):
        res = []
        if len(A) > 0:
            if A[0] == B:
                return [[A[0]]]
            elif A[0] > B:
                return []
            subSumsA = self.combinationSum(A, B - A[0])
            subSumsB = self.combinationSum(A[1:], B)
            if subSumsA != []:
                res += [[A[0]] + x for x in subSumsA]
            if subSumsB != []:
                res += subSumsB
        return res

    def combinationSum(self, A, B):
        return self.combSum(sorted(list(set(A))), B)
