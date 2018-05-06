class Solution:
    # @param A : integer
    # @return a list of integers
    def isprime(self, a):
        if a < 2:
            return False
        i = 2
        while i * i <= a:
            if a % i == 0:
                return False
            i += 1
        return True

    def primesum(self, A):
        for i in xrange(2, A / 2  + 1):
            b = A - i
            if self.isprime(i) and self.isprime(b):
                return i, b