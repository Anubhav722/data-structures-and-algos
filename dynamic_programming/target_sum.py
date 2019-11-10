# https://www.educative.io/courses/grokking-dynamic-programming-patterns-for-coding-interviews/7nAOY4oy64A

def target_sum(A, cur_index, ans, cur_sum):
    if cur_sum == ans:
        return 1
    if cur_index >= len(A):
        return 0
    sum1 = 0
    if A[cur_index] <= ans:
        sum1 = target_sum(A, cur_index+1, ans, cur_sum+A[cur_index])
    sum2 = target_sum(A, cur_index+1, ans, cur_sum)
    return sum1+sum2

def solution(A, S):
    ans = (sum(A) + S) / 2
    return target_sum(A, 0, ans, 0)

