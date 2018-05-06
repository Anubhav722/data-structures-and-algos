"""
Given an integer, convert it to a roman numeral, and return a string corresponding to its roman numeral version

Input is guaranteed to be within the range from 1 to 3999.

Example :

Input : 5
Return : "V"

Input : 14
Return : "XIV"
"""


class Solution:
    # @param A : integer
    # @return a strings
    def intToRoman(self, A):
        value = ""
        if A < 1:
            return value
        MAP = {
            0: "",
            1: "I",
            5: "V",
            10: "X",
            50: "L",
            100: "C",
            500: "D",
            1000: "M"
        }
        A = str(A)
        l = len(A)
        for pos in range(l):
            modulo_by = pow(10, l - pos - 1)
            current_char = int(A[pos])
            nearest_value = modulo_by
            if current_char > 3:
                nearest_value = modulo_by * 5
                if current_char > 8:
                    nearest_value = modulo_by * 10
                    value += MAP[modulo_by] + MAP[nearest_value]
                elif current_char >= 5:
                    value += MAP[nearest_value]
                    value += MAP[modulo_by] * (current_char - 5)
                else:
                    value += MAP[modulo_by] + MAP[nearest_value]
            else:
                value += MAP[nearest_value] * current_char
        return value
