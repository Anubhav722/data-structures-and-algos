
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def get_ans(self, A, stack, index):
        # import ipdb; ipdb.set_trace()
        _len = len(stack) - 1
        _value = A[index]
        rt = -1
        while _len >= 0:
            if A[stack[_len]] <= _value:
                rt = index - stack[_len]
            else:
                return rt
            _len -= 1
        return rt

    def maximumGap(self, A):
        # import ipdb; ipdb.set_trace()
        if not A or len(A) == 1:
            return 0

        stack = [0]
        ans = 0
        for i in range(1, len(A)):
            top = A[stack[-1]]
            if A[i] >= top:
                rt = self.get_ans(A, stack, i)
                ans = max(ans, rt)
            else:
                stack.append(i)
        return ans



# Try it out


# def maxgap(A):
#     if not A or len(A) == 1:
#         return 0

#     n = len(A)
#     # max_possible_length = n-1

#     ans = 0
#     for i in range(n):
#         for j in range(n-1, 0, -1):

#             if A[j] >= A[i]:
#                 _sum = j - i

#                 # if _sum == max_possible_length:
#                 #     return _sum

#                 ans = max(_sum, ans)

#     return ans


