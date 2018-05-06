# compute (x^n)%d


class Solution:
    # @param x : integer
    # @param n : integer
    # @param d : integer
    # @return an integer
    def pow(self, x, n, d):
        if n == 0:
            return 1%d
        temp = self.pow(x, n/2, d)
        return (temp*temp)%d if n%2==0 else (x*temp*temp)%d