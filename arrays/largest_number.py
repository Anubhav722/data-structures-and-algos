
# No idea how this works


class Solution:
    # @param A : tuple of integers
    # @return a strings

    def largestNumber(self, A):
        maxlen = len(str(max(A)))
        if all(v == 0 for v in A):
            return '0'
        import ipdb; ipdb.set_trace()
        return ''.join(sorted((str(v) for v in A), reverse=True,
                          key=lambda i: i*(maxlen * 2 // len(i))))




# Code below doesn't work

# class Solution:
#     # @param A : tuple of integers
#     # @return a strings
#     def largestNumber(self, A):
#         n = len(A)
#         arr = []
#         A = list(A)
#         if A.count(0) == n:
#             return '0'
#         for i in A:
#             z = i
#             r = 0
#             while z != 0:
#                 r = z % 10
#                 z = z/10
#             arr.append(r)
#         new_arr = []
#         while arr.count(None) != n:
#             if arr.count(max(arr)) > 1:
#                 indeces = [i for i, x in enumerate(arr) if x == max(arr)]
#                 last_index = -1
#                 import ipdb; ipdb.set_trace()
#                 for i in indeces:
#                     if int(str(A[i] % 10**(len(str(A[i]))-1))[0]) > last_index:
#                         last_index = int(str(A[i] % 10**(len(str(A[i]))-1))[0])
#                         element = A[i]

#                 new_arr.append(element)
#                 index = A.index(element)
#                 arr[index] = None
#                 A[index] = None

#             else:
#                 index = arr.index(max(arr))
#                 new_arr.append(A[index])
#                 arr[index] = None
                
#         return "".join(map(str, new_arr))