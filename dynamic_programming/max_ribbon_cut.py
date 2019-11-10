# https://www.educative.io/courses/grokking-dynamic-programming-patterns-for-coding-interviews/YQVZJx1k0WY
# The solution i have done is incorrect

def max_ribbon_cut(A, length, cur_index):
    if length == 0:
        return 1
    if cur_index >= len(A):
        return 0

    cut1 = 0
    if A[cur_index] <= length:
        if not max_ribbon_cut(A, length - A[cur_index], cur_index):
            cut1 += 1
        #cut1 = 1 + max_ribbon_cut(A, length - A[cur_index], cur_index)
    cut2 = max_ribbon_cut(A, length, cur_index+1)
    return max(cut1, cut2)

def solution(A, length):
    return max_ribbon_cut(A, length, 0)
