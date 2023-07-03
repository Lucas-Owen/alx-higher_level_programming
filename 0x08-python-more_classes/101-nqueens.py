#!/usr/bin/python3
"""This module defines a script to solve N queens puzzle

Usage: nqueens N
Where n is an integer greater than or equal to 4
"""


class NQueens():
    """Class to solve the N Queens puzzle"""
    def __init__(self, N=4):
        self.N = N

    @property
    def N(self):
        return self.__N

    @N.setter
    def N(self, value):
        try:
            value = int(value)
        except Exception:
            raise TypeError('N must be a number')
        if value < 4:
            raise ValueError('N must be at least 4')
        self.__N = value

    def solve(self):
        """Finds solutions to the puzzle by backtracking"""
        chessboard = [[False] * self.N for _ in range(self.N)]
        self.backtrack(chessboard, [])

    def backtrack(self, chessboard, currSoln):
        """Runs the actual backtracking algorithm"""
        if len(currSoln) == self.N:
            print(currSoln)
            return True
        for row in range(self.N):
            for col in range(self.N):
                if currSoln:
                    if currSoln[-1][0] != row - 1:
                        continue
                if self.valid(chessboard, row, col):
                    currSoln.append([row, col])
                    chessboard[row][col] = True
                    self.backtrack(chessboard, currSoln)
                    chessboard[row][col] = False
                    currSoln.pop()
        return False

    def valid(self, chessboard, row, col):
        """Checks if a queen can be placed at specified index"""
        if row >= self.N or col >= self.N or row < 0 or col < 0:
            return False
        for i in range(self.N):
            if chessboard[row][i] or chessboard[i][col]:
                return False
        for i, j in zip(range(row, self.N), range(col, self.N)):
            if chessboard[i][j]:
                return False
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if chessboard[i][j]:
                return False
        for i, j in zip(range(row, self.N), range(col, -1, -1)):
            if chessboard[i][j]:
                return False
        for i, j in zip(range(row, -1, -1), range(col, self.N)):
            if chessboard[i][j]:
                return False
        return True


if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        exit(1)
    nqueens = None
    try:
        nqueens = NQueens(sys.argv[1])
    except Exception as e:
        print(e)
        exit(1)
    nqueens.solve()
