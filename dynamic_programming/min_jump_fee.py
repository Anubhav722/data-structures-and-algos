def minJumps(A, cur_index):
    if cur_index >= len(A):
        return 0
    step1 = 0
    step2 = 0
    step3 = 0

    step1 = A[cur_index] + minJumps(A, cur_index+1)
    step2 = A[cur_index] + minJumps(A, cur_index+2)
    step3 = A[cur_index] + minJumps(A, cur_index+3)
    return min(step1, step2, step3)

def solution(A):
    return minJumps(A, 0)
