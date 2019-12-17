# https://www.educative.io/courses/grokking-dynamic-programming-patterns-for-coding-interviews/YQy7Lx79R0K

# stair1 = 0
# stair2 = 0
# stair3 = 0

def recur(A, cur_stair):
    if cur_stair == A:
        return 1
    if cur_stair > A:
        return 0
    stair1 = 0
    stair2 = 0
    stair3 = 0
    stair1 += recur(A, cur_stair+1)
    stair2 += recur(A, cur_stair+2)
    stair3 += recur(A, cur_stair+3)
    return stair1 + stair2 + stair3

def solution(A):
    return recur(A, 0)
