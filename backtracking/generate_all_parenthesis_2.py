# https://www.interviewbit.com/problems/generate-all-parentheses-ii/

# Crazy recursion solution.


class Solution:
    # @param A : integer
    # @return a list of strings
    def generateParenthesis(self, A):
        current = []

        def generate(parenthesis, A, open, close):
            if close == A:
                current.append(parenthesis)
            else:
                if open > close:
                    generate(parenthesis + ")", A, open, close + 1)
                if open < A:
                    generate(parenthesis + "(", A, open + 1, close)

        if A > 0:
            generate("", A, 0, 0)
        current.reverse()
        return current
