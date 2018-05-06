class Solution:
    # @param A : integer
    # @return a list of integers
    def getRow(self, A):
        arr = [[0]*_ for _ in range(1,A+2)]

        for i in range(A+1):
            for x in range(len(arr[i])):
                if i == 0:
                    arr[0][0] = 1
                    break
                elif i == 1:
                    arr[1][0] = 1
                    arr[1][1] = 1
                    break
                else:
                    if x == 0 or x == len(arr[i])-1:
                        arr[i][x] = 1
                    # arr[i][0] = 1
                    else:
                        arr[i][x] = arr[i-1][x-1] + arr[i-1][x]

            if A == i:
                return arr[i]
        # return arr