# https://www.interviewbit.com/problems/letter-phone/


class Solution:
    # @param A : string
    # @return a list of strings
    def letterCombinations(self, A):
        cur = ""
        res = []
        phone_map = {"1": "1", "2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno",
                     "7": "pqrs", "8": "tuv", "9": "wxyz", "0": "0"}

        if not A:
            return []
        self.letterCombinationsHelper(cur, res, A, phone_map)
        return sorted(res)

    def letterCombinationsHelper(self, cur, res, A, phone_map):
        if not A:
            res.append(cur)
            return

        # iterate for all phone maps
        for s in phone_map[A[0]]:
            cur = cur + s
            self.letterCombinationsHelper(cur, res, A[1:], phone_map)

            # Backtrack the string
            cur = cur[:-1]
