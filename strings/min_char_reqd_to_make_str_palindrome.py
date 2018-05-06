# You are given a string. The only operation allowed is to insert characters in the beginning of the string. How many minimum characters are needed to be inserted to make the string a palindrome string

# Example:
# Input: ABC
# Output: 2
# Input: AACECAAAA
# Output: 2


class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        if A == A[::-1]:
            return 0

        j = len(A) - 1
        while j >= 0:
            B = A[:j]
            if B == B[::-1]:
                return len(A) - j
            j -= 1
        return len(A) - 1
