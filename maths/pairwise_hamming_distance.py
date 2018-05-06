# Didn't get it at all.

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def hammingDistance(self, A):
    	import ipdb; ipdb; ipdb.set_trace()
        N = len(A)
        counter1s = [0] * 64
        for num in A:
            bit = 0
            while num:
                if num & 1:
                    counter1s[bit] += 1
                num /= 2
                bit += 1
        return (2 * sum([bitcount * (N - bitcount) for bitcount in counter1s])) % 1000000007


# class Solution:
#     # @param A : tuple of integers
#     # @return an integer
#     def hammingDistance(self, A):
#     	import ipdb; ipdb.set_trace()
#         n = len(A)
#         c=0
#         for i in range(32):
#             mask = 1<<i
#             t = 0
#             for a in A:
#                 if(mask&a):
#                     t += 1
#             c += (t*(n-t))
#         return (2*c)%1000000007
