def coin_change(D, A):
    return recur(D, A, 0)

def recur(D, A, cur_index):
    if A == 0:
        return 1
    if cur_index >= len(D):
        return 0
    w1 = 0
    if D[cur_index] <= A:
        w1 = recur(D, A-D[cur_index], cur_index)
    w2 = recur(D, A, cur_index+1)
    return w1 + w2
