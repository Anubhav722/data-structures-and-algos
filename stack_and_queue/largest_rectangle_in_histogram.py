# Testcase:
# [ 90, 58, 69, 70, 82, 100, 13, 57, 47, 18 ]


class Solution:
    # @param A : list of integers
    # @return an integer
    def largestRectangleArea(self, A):
        stack = []
        n = len(A)
        ret = 0
        tp = -1
        area_with_top = -1
        i = 0
        import ipdb; ipdb.set_trace()
        while i < n:
            if len(stack) == 0 or A[i] >= A[stack[-1]]:
                stack.append(i)
                i += 1
            else:
                tp = stack.pop()
                area_with_top = A[tp]*(i if len(stack) == 0 else i - stack[-1] - 1)
                if ret < area_with_top:
                    ret = area_with_top
        while len(stack) != 0:
            tp = stack.pop()
            area_with_top = A[tp]*(i if len(stack) == 0 else i - stack[-1] - 1)
            if ret < area_with_top:
                ret = area_with_top

        return ret
