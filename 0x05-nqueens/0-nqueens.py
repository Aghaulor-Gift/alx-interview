#!/usr/bin/python3
""" The N queens puzzle is the challenge of placing
N non-attacking queens on an N×N chessboard"""
import sys


def is_safe(board, row, col, N):
    """Check if it's safe to place a queen at board[row][col]."""
    # Check the left side of the current row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check the upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check the lower diagonal on the left side
    for i, j in zip(range(row, N), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens_util(board, col, N, solutions):
    """Utilize backtracking to solve the N queens problem."""
    if col >= N:
        # A solution is found; add it to the solutions list
        solution = []
        for i in range(N):
            for j in range(N):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return True

    res = False
    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1  # Place the queen
            res = solve_nqueens_util(board, col + 1, N, solutions) or res
            board[i][col] = 0  # Backtrack

    return res


def solve_nqueens(N):
    """Solve the N queens problem and print all solutions."""
    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []
    solve_nqueens_util(board, 0, N, solutions)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(N)
