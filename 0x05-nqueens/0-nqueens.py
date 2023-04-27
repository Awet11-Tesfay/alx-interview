#!/usr/bin/python3
""" The nqueens puzzle is the challenge of placing N
"""
import sys


import sys

def solveNQueens(n):
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    board = [-1] * n
    solve(board, 0, n)

def solve(board, col, n):
    if col == n:
        print_board(board)
        return
    for i in range(n):
        if is_valid(board, col, i):
            board[col] = i
            solve(board, col + 1, n)

def is_valid(board, col, row):
    for i in range(col):
        if board[i] == row or \
            board[i] - i == row - col or \
            board[i] + i == row + col:
            return False
    return True

def print_board(board):
    for row in board:
        line = ""
        for i in range(len(board)):
            if i == row:
                line += "Q"
            else:
                line += "."
        print(line)
    print()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    solveNQueens(n)
