# 1   2   3
# 4   5   6
# 7   8   9
#     0






def calculatePathSum(S, N):
    # S is the start value
    # N is the no. of hops
    if N == 0:
        return 1
    hashmap = {1: [8, 6], 2: [7, 9], 3: [8, 4], 4: [3, 9, 0], 5: [], 6: [1, 7, 0], 7: [2, 6], 8: [1, 3], 9: [2, 4], 0: [4, 6]}
    count = 0
    for val in hashmap[S]:
        count += calculatePathSum(val, N-1)
    return count
