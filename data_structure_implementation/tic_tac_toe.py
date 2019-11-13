# http://buttercola.blogspot.com/2016/06/leetcode-348-design-tic-tac-toe.html

# Time:  O(1), per move.
# Space: O(n^2)

class TicTacToe(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.size = n
        self.rows = [[0, 0] for _ in range(n)]
        self.cols = [[0, 0] for _ in range(n)]
        self.diagonal = [0, 0]
        self.anti_diagonal = [0, 0]

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """

        i = player - 1
        self.rows[row][i] += 1
        self.cols[col][i] += 1
        if row == col:
            self.diagonal[i] += 1

        if col == len(self.rows) - row - 1:
            self.anti_diagonal[i] += 1

        if self.rows[row][i] == self.size:
            return player
        elif self.cols[col][i] == self.size:
            return player
        elif self.diagonal[i] == self.size:
            return player
        elif self.anti_diagonal[i] == self.size:
            return player
        else:
            return 0


#        if any(self.rows[row][i] == self.size,
#               self.cols[col][i] == self.size,
#               self.diagonal[i] == self.size,
#               self.anti_diagonal[i] == self.size):
#            return player

#        return 0

