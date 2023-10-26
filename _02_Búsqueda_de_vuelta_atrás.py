# _*_ coding: utf-8 _*_
#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_

def is_safe(board, row, col, N):
    # Verifica si es seguro colocar una reina en la posición (row, col)
    # en el tablero dado
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens(N):
    board = [[0] * N for _ in range(N)]

    def solve(row):
        if row == N:
            # Se ha encontrado una solución
            for i in range(N):
                for j in range(N):
                    print(board[i][j], end=" ")
                print()
            print()
            return

        for col in range(N):
            if is_safe(board, row, col, N):
                board[row][col] = 1
                solve(row + 1)
                board[row][col] = 0

    solve(0)

if __name__ == "__main__":
    N = 4  # Tamaño del tablero (N x N)
    solve_n_queens(N)
