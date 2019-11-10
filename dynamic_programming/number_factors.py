# https://www.educative.io/courses/grokking-dynamic-programming-patterns-for-coding-interviews/NE52PnMY376

def number_factors(A, cur_sum):
    if cur_sum == A:
        return 1
    if cur_sum > A:
        return 0
    add1 = 0
    add3 = 0
    add4 = 0
    add1 += number_factors(A, cur_sum + 1)
    add3 += number_factors(A, cur_sum + 3)
    add4 += number_factors(A, cur_sum + 4)
    return add1 + add3 + add4

def solution(A):
    return number_factors(A, 0)
