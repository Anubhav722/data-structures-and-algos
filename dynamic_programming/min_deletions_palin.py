# https://www.educative.io/courses/grokking-dynamic-programming-patterns-for-coding-interviews/gkX4prBkRLj

def min_deletions(A, start_index, end_index):
    if start_index > end_index:
        return 0
    if start_index == end_index:
        return 1
    if A[start_index] == A[end_index]:
        return 2 + min_deletions(A, start_index + 1, end_index - 1)
    c1 = min_deletions(A, start_index+1, end_index)
    c2 = min_deletions(A, start_index, end_index - 1)
    return max(c1, c2)

def solution(A):
    return len(A) - min_deletions(A, 0, len(A)-1)
