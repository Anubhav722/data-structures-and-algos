"""
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.

Read more details about roman numerals at Roman Numeric System

Example :

Input : "XIV"
Return : 14
Input : "XX"
Output : 20
"""


class Solution:
    # @param A : string
    # @return an integer
    def romanToInt(self, A):
        bank = {'X': 10, 'V' : 5, 'I' : 1, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}

        res = 0
        for i in xrange(0, len(A)):
            cur = bank[A[i]]
            if i+1 < len(A) and cur < bank[A[i+1]]:
                res -= cur
            else:
                res+= cur

        return res