# A better solution which doesn't use up extra memory.
# Has less time complexity too.

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def findMedian(self, A):
        for i in range(1,len(A)):
            A[0].extend(A[i])
            A[i] = None
        A = sorted(A[0])
        return A[len(A)//2]





# SOLUTION BY ME WHICH ACTUALLY WORKED. 
# but time complexity is not good.


# class Solution:
#     # @param A : list of list of integers
#     # @return an integer
#     def findMedian(self, A):
#         n = len(A)
#         new_arr = []

#         for i in A:
#             for j in i:
#                 new_arr.append(j)

#         new_arr.sort()
#         return new_arr[len(new_arr)/2]
