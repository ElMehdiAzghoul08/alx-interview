#!/usr/bin/python3

"""N Queens solver"""
import sys


def is_safe(board, row, col, n):
    """Check queen safety"""
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(board, col, n):
    """Recursive backtracking solver"""
    if col >= n:
        solution = []
        for i in range(n):
            for j in range(n):
                if board[i][j] == 1:
                    solution.append([i, j])
        return [solution]

    solutions = []
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            solutions.extend(solve_nqueens(board, col + 1, n))
            board[i][col] = 0

    return solutions


def print_solutions(solutions):
    """Print board solutions"""
    for solution in solutions:
        print(solution)


def nqueens(n):
    """Main N Queens solver"""
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = solve_nqueens(board, 0, n)
    solutions.sort()
    print_solutions(solutions)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
        nqueens(n)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
