class Solution:
    # @param A : list of integers
    # @return a list of integers
    def prevSmaller(self, A):
        if not A:
            return A
        s = []
        ans = []
        for i in range(len(A)):
            while s and s[-1] >= A[i]:
                s.pop()

            if not s:
                ans.append(-1)
            else:
                ans.append(s[-1])

            s.append(A[i])
        return ans


# Partially Correct Answer. Time limit exceeded.


# class Solution:
#     # @param A : list of integers
#     # @return a list of integers
#     def prevSmaller(self, A):
#         ans = []
#         # import ipdb; ipdb.set_trace()
#         for i in range(len(A)):
#             if i == 0:
#                 ans.append(-1)
#                 continue
#             if A[i] > min(A[:i]):
#                 j = i - 1
#                 while j != 0:
#                     if A[j] < A[i]:
#                         ans.append(A[j])
#                         break
#                     j -= 1
#                 else:
#                   ans.append(A[j])
#             else:
#                 ans.append(-1)
#         return ans
