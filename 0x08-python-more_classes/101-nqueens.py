#!/usr/bin/python3
""" Solves a Chess puzzle of proper positioning and backtracking"""


import sys


def is_safe(board, row, col, N):
    """Check if it's safe to place a queen at a given position."""
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    i = row - 1
    j = col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    i = row - 1
    j = col + 1
    while i >= 0 and j < N:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1

    return True


def solve_nqueens(N):
    """Solve the N-Queens problem and return all possible answers."""
    board = [['.' for r in range(N)] for r in range(N)]
    answers = []

    def backtrack(row):
        """Backtracking function to place queens recursively."""
        if row == N:
            answers.append([''.join(row) for row in board])
            return

        for col in range(N):
            if is_safe(board, row, col, N):
                board[row][col] = 'Q'
                backtrack(row + 1)
                board[row][col] = '.'

    backtrack(0)

    return answers


if __name__ == '__main__':
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

    answers = solve_nqueens(N)

    for answer in answers:
        for row in answer:
            print(row)
        print()
