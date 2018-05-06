"""
Given a string S, find the longest palindromic substring in S.

Substring of string S:

S[i...j] where 0 <= i <= j < len(S)

Palindrome string:

A string which reads the same backwards. More formally, S is palindrome if reverse(S) = S.

Incase of conflict, return the substring which occurs first ( with the least starting index ).

Example :

Input : "aaaabaaa"
Output : "aaabaaa"
"""


class Solution:
    # @param A : string
    # @return a strings
    def longestPalindrome(self, A):
        rev = A[::-1]
        l = len(A)
        while l > 0:
            for i in xrange(0, len(A) - l + 1):
                half = int(l / 2)
                left = A[i : i + half]
                right = rev[len(A) - (i + l) : len(A) - (i + l - half)]
                if left == right:
                    return A[i:i+l]
            l -= 1
        return None
