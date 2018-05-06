# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

# Example:

# "A man, a plan, a canal: Panama" is a palindrome.

# "race a car" is not a palindrome.

# Return 0 / 1 ( 0 for false, 1 for true ) for this problem


import re


class Solution:
    # @param A : string
    # @return an integer
    def isPalindrome(self, A):
        regex = re.compile('[^a-zA-Z1-9]')
        new_str = regex.sub('', A).lower()
        if new_str == new_str[::-1]:
            return 1
        return 0
