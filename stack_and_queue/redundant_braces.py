class Solution:
    # @param A : string
    # @return an integer
    def braces(self, A):
        stack = []
        # import ipdb; ipdb.set_trace()
        for el in A:
            if el == "(":
                stack.append(el)
            elif el in ['+', '-', '/', '*']:
                stack.append("exp")
            elif el == ")":
                if stack[-1] == "exp":
                    stack.pop()
                    stack.pop()
                else:
                    return 1
        else:
            return 0
