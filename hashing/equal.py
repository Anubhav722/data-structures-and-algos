# Failing for test case: [ 1, 1, 1, 1, 1 ], expected answer is: [0,1,2,3]
# in place of which [] is returned.


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def equal(self, A):

        hash_map = {}
        for i in range(len(A)):
            for j in range(i+1, len(A)):
                if A[i] + A[j] in hash_map:
                    _sum = A[i] + A[j]

                    hash_map[A[i]+A[j]].append((i,j))
                else:
                    hash_map[A[i]+A[j]] = [(i,j)]
        solution = []

        for i, j in hash_map.iteritems():
            if len(j) > 1:
                if not solution:
                    if j[0][0] < j[0][1] and j[1][0] < j[1][1] and j[0][1] < j[1][0] and j[0][1] != j[1][1] and j[0][1] != j[1][0]:
                        solution = [j[0][0], j[0][1], j[1][0], j[1][1]]
                else:
                    if j[0][0] < solution[0]:
                        solution = [j[0][0], j[0][1], j[1][0], j[1][1]]
                    elif j[0][0] == solution[0] and j[0][1] < solution[1]:
                        solution = [j[0][0], j[0][1], j[1][0], j[1][1]]
                    elif j[0][0] == solution[0] and j[0][1] == solution[1] and j[1][0] < solution[2]:
                        solution = [j[0][0], j[0][1], j[1][0], j[1][1]]
                    elif j[0][0] == solution[0] and j[0][1] == solution[1] and j[1][0] == solution[2] and j[1][1] < solution[3]:
                        solution = [j[0][0], j[0][1], j[1][0], j[1][1]]

        return solution