print("Enter the number of queens")
N = int(input())

# Initialize the board as an NxN grid filled with zeros
board = [[0] * N for _ in range(N)]

def is_safe(row, col):
    # Check previous rows in the same column and diagonals
    for i in range(row):
        if board[i][col] == 1 or \
           (col - row + i >= 0 and board[i][col - row + i] == 1) or \
           (col + row - i < N and board[i][col + row - i] == 1):
            return False
    return True

def solve(n):
    if n == 0:
        return True
    row = N - n
    for col in range(N):
        if is_safe(row, col):
            board[row][col] = 1
            if solve(n - 1):
                return True
            board[row][col] = 0  # Backtrack
    return False

solve(N)
for row in board:
    print(row)
