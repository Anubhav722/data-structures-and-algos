# The count-and-say sequence is the sequence of integers beginning as follows:

# 1, 11, 21, 1211, 111221, ...
# 1 is read off as one 1 or 11.
# 11 is read off as two 1s or 21.

# 21 is read off as one 2, then one 1 or 1211.

# Given an integer n, generate the nth sequence.

# Note: The sequence of integers will be represented as a string.

# Example:

# if n = 2,
# the sequence is 11.


from itertools import groupby


class Solution:
    # @param A : integer
    # @return a strings
    def countAndSay(self, A):
        current = '1'
        for i in range(1, A):
            current = "".join([str(len(list(v))) + k for k, v in groupby(current)])
        return current
