# Will be done using Eratosthenes

# Let us say we are given n number
# We create an array which contains all number starting from 2, 3 ... n
# We start with 2 which is prime and delete all multiples of 2 from the array.
# Then we go to next element which is 3 and delete its multiples from array.


# Sieve of Eratosthenes

class Solution:
    # @param A : integer
    # @return a list of integers
    def sieve(self, A):

        prime_numbers = [1 for _ in range(A+1)]
        prime_numbers[0] = 0
        prime_numbers[1] = 0

        for i in range(2, A+1):
            if prime_numbers[i] == 1:
                j = 2
                while (j*i <= A):
                    prime_numbers[i*j] = 0
                    j += 1
        return [prime for prime in range(len(prime_numbers)) if prime_numbers[prime] == 1]