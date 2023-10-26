# _*_ coding: utf-8 _*_
#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_

import random

def is_conflict(board, row, col):
    # Verifica si una reina en la posición (row, col) tiene conflictos
    for i in range(col):
        if board[i] == row or \
           board[i] - i == row - col or \
           board[i] + i == row + col:
            return True
    return False

def min_conflicts(N, max_iterations):
    board = [random.randint(0, N-1) for _ in range(N)]

    for _ in range(max_iterations):
        conflicts = [0] * N

        for col in range(N):
            for row in range(N):
                if board[col] == row:
                    continue

                new_board = board[:]
                new_board[col] = row
                new_conflicts = sum(1 for c in range(N) if is_conflict(new_board, c, new_board[c]))

                if new_conflicts < conflicts[col]:
                    board[col] = row
                    conflicts[col] = new_conflicts

        if sum(conflicts) == 0:
            return board

    return None

def print_solution(board):
    if board is None:
        print("No se encontró solución.")
        return

    N = len(board)
    for row in range(N):
        line = ["Q" if board[row] == col else "." for col in range(N)]
        print(" ".join(line))

if __name__ == "__main__":
    N = 8  # Tamaño del tablero (N x N)
    max_iterations = 1000

    solution = min_conflicts(N, max_iterations)
    print_solution(solution)
