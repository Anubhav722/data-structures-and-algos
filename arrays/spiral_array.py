# PRINTING A MATRIX IN A SPIRAL FORMAT.


class Solution:
    # @param A : tuple of list of integers
    # @return a list of integers
    def spiralOrder(self, A):
        topmost_row_index = 0
        bottomost_row_index = len(A) -1
        leftmost_column_index = 0
        rightmost_column_index = len(A[0]) - 1
        direction = 0 
        # 0 means left to right
        # 1 means top to bottom
        # 2 means right to left
        # 3 means bottom to top

        while (topmost_row_index <= bottomost_row_index and leftmost_column_index <= rightmost_column_index):
            if direction == 0:
                for i in xrange(leftmost_column_index, rightmost_column_index+1):
                    print (A[topmost_row_index][i])
                topmost_row_index += 1
                direction = 1
            elif direction == 1:
                for i in xrange(topmost_row_index, bottomost_row_index+1):
                    print (A[i][rightmost_column_index])
                rightmost_column_index -= 1
                direction = 2
            elif direction == 2:
                for i in xrange(rightmost_column_index, leftmost_column_index-1, -1):
                    print (A[bottomost_row_index][i])
                bottomost_row_index -= 1
                direction = 3
            elif direction == 3:
                for i in xrange(bottomost_row_index, topmost_row_index-1, -1):
                    print (A[i][leftmost_column_index])
                leftmost_column_index += 1
                direction = 0
