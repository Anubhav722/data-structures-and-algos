class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def twoSum(self, A, B):
        hash_map = {}

        for i in range(len(A)):

            if A[i] in hash_map:
                return [hash_map[A[i]]+1, i+1]
            else:
                if B-A[i] not in hash_map:
                    hash_map[B-A[i]] = i

        return []
