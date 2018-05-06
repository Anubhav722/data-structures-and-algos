
# Time Complexity: O(n**.5)


class Solution:
    # @param A : integer
    # @return a list of integers
    def allFactors(self, A):
        factors = []
        if A == 1:
            return [1]
        upperLimit = A**.5
        for i in range(1, int(upperLimit)+1):
            if A % i == 0:
                factors.append(i)
                if i != upperLimit:
                    factors.append(A/i)
        return sorted(factors)


# Time COmplexity: O(n)


# class Solution:
#     # @param A : integer
#     # @return a list of integers
#     def allFactors(self, A):
#         factors = []
#         for i in range(1, A/2 + 1):
#             if A % i == 0:
#                 factors.append(i)
#         return factors+1
