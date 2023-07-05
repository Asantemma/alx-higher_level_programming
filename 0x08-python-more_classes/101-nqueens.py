#!/usr/bin/python3
"""
N queens backtracking program to find solutions for placing N queens
on an NxN grid such that they are all in non-attacking positions
"""


import sys


if __name__ == "__main__":
    board = []
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    if argv[1].isdigit() is False:
        print("N must be a number")
        exit(1)
    n = int(argv[1])
    if n < 4:
        print("N must be at least 4")
        exit(1)

# initializing the chessboard
for i in range(n):
    board.append([i, None])


def queen_exists_in_same_column(column):
    """Checks if a queen already exists in the given column"""
    for row in range(n):
        if column == board[row][1]:
            return True
    return False


def reject_placement(row, column):
    """Determine whether or not to reject the queen placement"""
    if queen_exists_in_same_column(column):
        return False
    i = 0
    while(i < row):
        if abs(board[i][1] - column) == abs(i - row):
            return False
        i += 1
    return True


def clear_board(row):
    """Clear the board from the point of failure onwards"""
    for i in range(row, n):
        board[i][1] = None


def find_solutions(row):
    """Recursive backtracking function to find the solutions"""
    for column in range(n):
        clear_board(row)
        if reject_placement(row, column):
            board[row][1] = column
            if (row == n - 1):
                print(board)
            else:
                find_solutions(row + 1)


# Start the recursive process at the first row (row 0)
find_solutions(0)
