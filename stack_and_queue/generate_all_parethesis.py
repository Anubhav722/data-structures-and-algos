"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

Return 0 / 1 ( 0 for false, 1 for true ) for this problem

"""


class Solution:
    # @param A : string
    # @return an integer
    def isValid(self, A):
        s = []

        for i in range(len(A)):
            if A[i] in ['(', '[', '{']:
                s.append(A[i])
            else:
                if len(s) == 0:
                    return 0
                elif A[i] == '}' and ( s[-1] == '[' or s[-1] == '('):
                    return 0
                elif A[i] == ']' and ( s[-1] == '(' or s[-1] == '{' ):
                    return 0
                elif A[i] == ')' and ( s[-1] == '{' or s[-1] == '[' ):
                    return 0
                else:
                    s.pop()
        return len(s) == 0


# Solved this problem using iteration and counter
# Case where it breaks is as follows: )(, [(])

# class Solution:
#     # @param A : string
#     # @return an integer
#     def isValid(self, A):

#         a_count = 0
#         b_count = 0
#         c_count = 0

#         for i in range(len(A)):
#             if A[i] == "(":
#                 a_count += 1
#             elif A[i] == ")":
#                 a_count -= 1
#             elif A[i] == "{":
#                 b_count += 1
#             elif A[i] == "}":
#                 b_count -= 1
#             elif A[i] == "[":
#                 c_count += 1
#             elif A[i] == "]":
#                 c_count -= 1
#         if a_count == 0 and b_count == 0 and c_count == 0:
#             return 1
#         return 0
