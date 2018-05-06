class Kstacks:

    def __init__(self, k, n):
        self.arr = [None] * k * n
        # self.size = len(self.arr)
        self.stack_size = n
        self.top = [-1] * k
        self.next = [n * i for i in range(k)]

    def push(self, stack, item):
        if self.top[stack - 1] < self.stack_size - 1:
            self.arr[self.next[stack - 1]] = item
            self.next[stack - 1] += 1
            self.top[stack - 1] += 1
        else:
            print "Stack OverFlow"
            return -1

    def pop(self, stack):
        if self.top[stack - 1] != -1:
            x = self.arr[self.next[stack - 1] - 1]
            self.arr[self.next[stack - 1] - 1] = None
            self.next[stack - 1] -= 1
            self.top[stack - 1] -= 1
            return x
        else:
            print "Stack UnderFlow"
            return -1

# O(N) TIME COMPLEXITY WITH LESS SPACE COMPLEXITY
# class KStack:
#     """docstring for KStack __init__(self, arg)"""
#         def __init__(self, k, n):
#             self.arr = [None]*k*n
#             self.size = n

#         def push(self, stack_num, k):

#             s = stack_num*n

#             if self.arr[s-1] != None:
#                 return

#             for i in range(((stack_num-1)*self.size), s):
#                 if self.arr[i] == None:
#                     self.arr[i] = k

#                     return
#             return "OverFlow"

#         def pop(self, stack):

#             s = (stack_n*n)-1

#             self.arr[s] = None

#             return


