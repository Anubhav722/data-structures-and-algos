class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generateMatrix(self, A):

        # creates a referential array don't use it.
        # spiral_matrix = [[0]*A]*A
        spiral_matrix = [ [0]*A for _ in xrange(A) ]
        topmost_row_index = 0
        bottomost_row_index = A-1
        leftmost_column_index = 0
        rightmost_column_index = A-1
        direction = 0
        value = 1

        while (topmost_row_index <= bottomost_row_index and leftmost_column_index <= rightmost_column_index):
            if direction == 0:
                for i in range(leftmost_column_index, rightmost_column_index+1):
                    spiral_matrix[topmost_row_index][i] = value
                    value += 1
                topmost_row_index += 1
                direction = 1
            elif direction == 1:
                for i in range(topmost_row_index, bottomost_row_index+1):
                    spiral_matrix[i][rightmost_column_index] = value
                    value += 1
                rightmost_column_index -= 1
                direction = 2
            elif direction == 2:
                for i in range(rightmost_column_index, leftmost_column_index-1, -1):
                    spiral_matrix[bottomost_row_index][i] = value
                    value += 1
                bottomost_row_index -= 1
                direction = 3
            elif direction == 3:
                for i in range(bottomost_row_index, topmost_row_index-1, -1):
                    spiral_matrix[i][leftmost_column_index] = value
                    value += 1
                leftmost_column_index += 1
                direction = 0

        return spiral_matrix