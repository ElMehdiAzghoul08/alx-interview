#!/usr/bin/python3
"""N-Queens problem solver"""
import sys


def solve(row, size, cols, diag1, diag2, board):
    """Find N-Queens solutions"""
    if row == size:
        result = []
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 1:
                    result.append([i, j])
        print(result)
        return

    for col in range(size):
        if col in cols or (row + col) in diag1 or (row - col) in diag2:
            continue
        cols.add(col)
        diag1.add(row + col)
        diag2.add(row - col)
        board[row][col] = 1
        solve(row+1, size, cols, diag1, diag2, board)
        cols.remove(col)
        diag1.remove(row + col)
        diag2.remove(row - col)
        board[row][col] = 0


def queens(size):
    """Main solving function"""
    cols = set()
    diag1 = set()
    diag2 = set()
    board = [[0] * size for _ in range(size)]
    solve(0, size, cols, diag1, diag2, board)


if __name__ == "__main__":
    args = sys.argv
    if len(args) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(args[1])
        if n < 4:
            print("N must be at least 4")
            sys.exit(1)
        queens(n)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
