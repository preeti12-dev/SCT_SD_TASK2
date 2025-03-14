# Function to check if a number can be placed at the given position (row, col)
def is_safe(board, row, col, num):
    # Check if the number is already in the current row
    for x in range(9):
        if board[row][x] == num:
            return False

    # Check if the number is already in the current column
    for x in range(9):
        if board[x][col] == num:
            return False

    # Check if the number is already in the 3x3 grid
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False

    return True

# Function to solve the Sudoku using backtracking
def solve_sudoku(board):
    empty_cell = find_empty(board)
    
    # If there is no empty cell, the board is solved
    if not empty_cell:
        return True
    
    row, col = empty_cell

    # Try all numbers from 1 to 9
    for num in range(1, 10):
        if is_safe(board, row, col, num):
            board[row][col] = num

            # Recursively try to solve the rest of the board
            if solve_sudoku(board):
                return True

            # Backtrack if the current number doesn't work
            board[row][col] = 0

    return False

# Function to find the next empty cell
def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None

# Function to print the Sudoku board
def print_board(board):
    for row in board:
        print(" ".join(str(num) if num != 0 else '.' for num in row))

# Example Sudoku board (0 represents empty cells)
sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Solve the Sudoku puzzle
if solve_sudoku(sudoku_board):
    print("Sudoku puzzle solved!")
    print_board(sudoku_board)
else:
    print("No solution exists for the given Sudoku puzzle.")