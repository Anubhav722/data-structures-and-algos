# https://www.educative.io/courses/grokking-dynamic-programming-patterns-for-coding-interviews/NE0yNJ1rZy6
import sys

def min_coin_change(A, cur_index, target):
    if target == 0:
        return 0
    if cur_index >= len(A):
        return sys.maxint

    coin1 = sys.maxint
    if A[cur_index] <= target:
        coin1 = 1 + min_coin_change(A, cur_index, target-A[cur_index])
    coin2 = min_coin_change(A, cur_index+1, target)
    return min(coin1, coin2)

def solution(A, target):
    return min_coin_change(A, 0, target)


