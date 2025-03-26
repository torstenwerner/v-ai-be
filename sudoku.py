def print_grid(grid):
    """Prints the Sudoku grid in a readable format."""
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - ")  # Horizontal separator for boxes
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print(" | ", end="") # Vertical separator for boxes

            if j == 8:
                print(grid[i][j]) # Print number and newline at the end of a row
            else:
                # Print number and space, stay on the same line
                print(str(grid[i][j]) + " ", end="")

def find_empty(grid):
    """Finds the next empty cell (represented by 0) in the grid.
       Returns (row, col) tuple or None if no empty cell is found."""
    for r in range(9):
        for c in range(9):
            if grid[r][c] == 0:
                return (r, c)
    return None # No empty cells left

def is_valid(grid, num, pos):
    """Checks if placing 'num' at 'pos' (row, col) is valid."""
    row, col = pos

    # 1. Check Row
    # If the number 'num' is already present in the current row (excluding the position itself), return False
    for j in range(9):
        if grid[row][j] == num and col != j:
             return False

    # 2. Check Column
    # If the number 'num' is already present in the current column (excluding the position itself), return False
    for i in range(9):
        if grid[i][col] == num and row != i:
            return False

    # 3. Check 3x3 Box
    # Determine the top-left corner of the 3x3 box the position belongs to
    box_x_start = (col // 3) * 3
    box_y_start = (row // 3) * 3

    # Iterate through the 3x3 box
    for i in range(box_y_start, box_y_start + 3):
        for j in range(box_x_start, box_x_start + 3):
            # If the number 'num' is already present in the box (excluding the position itself), return False
            if grid[i][j] == num and (i, j) != pos:
                return False

    # If all checks pass, the placement is valid
    return True

def solve(grid):
    """Solves the Sudoku puzzle using backtracking."""
    find = find_empty(grid)
    if not find:
        return True  # Base case: No empty cells left, puzzle is solved!
    else:
        row, col = find # Get coordinates of the empty cell

    # Try numbers 1 through 9 for the empty cell
    for num in range(1, 10):
        # Check if placing 'num' at (row, col) is valid
        if is_valid(grid, num, (row, col)):
            # If valid, place the number
            grid[row][col] = num

            # Recursively call solve() for the next empty cell
            if solve(grid):
                return True # If the recursive call returns True, the puzzle is solved

            # Backtrack: If solve(grid) returned False, the placement was incorrect.
            # Reset the cell to 0 and try the next number in the loop.
            grid[row][col] = 0

    # If no number from 1-9 works for this cell, trigger backtracking by returning False
    return False

# --- How to Use ---
# 1. Define your Sudoku puzzle as a 9x9 list of lists.
# 2. Use 0 to represent empty cells.

# Example Puzzle:
puzzle = [
    [0, 0, 0, 0, 0, 0, 0, 0, 7],
    [6, 0, 0, 4, 2, 0, 0, 0, 0],
    [0, 0, 4, 9, 0, 1, 0, 0, 3],
    [0, 0, 0, 0, 0, 9, 7, 0, 0],
    [0, 0, 6, 0, 0, 8, 4, 0, 0],
    [8, 9, 1, 0, 0, 4, 0, 0, 0],
    [0, 0, 9, 0, 5, 6, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 8],
    [5, 0, 0, 0, 0, 0, 0, 0, 0]
]

print("Unsolved Puzzle:")
print_grid(puzzle)
print("\nSolving...\n")

# Solve the puzzle (modifies the 'puzzle' list in-place)
if solve(puzzle):
    print("Solved Puzzle:")
    print_grid(puzzle)
else:
    print("No solution exists for this puzzle.")

# Example of an unsolvable puzzle (invalid initial state)
# unsolvable_puzzle = [
#     [5, 3, 1, 1, 7, 0, 0, 0, 0], # Two 1s in first row
#     [6, 0, 0, 1, 9, 5, 0, 0, 0],
#     [0, 9, 8, 0, 0, 0, 0, 6, 0],
#     [8, 0, 0, 0, 6, 0, 0, 0, 3],
#     [4, 0, 0, 8, 0, 3, 0, 0, 1],
#     [7, 0, 0, 0, 2, 0, 0, 0, 6],
#     [0, 6, 0, 0, 0, 0, 2, 8, 0],
#     [0, 0, 0, 4, 1, 9, 0, 0, 5],
#     [0, 0, 0, 0, 8, 0, 0, 7, 9]
# ]
# print("\nTrying unsolvable puzzle:\n")
# if solve(unsolvable_puzzle):
#     print_grid(unsolvable_puzzle)
# else:
#     print("No solution exists.")