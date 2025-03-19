# Python program to generate a valid sudoku 
# with k empty cells
from Jeu import Jeu
from Sudoku import subdiv
import random 

# Returns false if given 3x3 block contains num
# Ensure the number is not used in the box
def unused_in_box(grid, row_start, col_start, num):
    for i in range(3):
        for j in range(3):
            if grid.terrain[row_start + i][col_start + j].occupant == num:
                return False
    return True
# Fill a 3x3 matrix
# Assign valid random numbers to the 3x3 subgrid
def fill_box(grid, row, col):
    for i in range(3):
        for j in range(3):
            while True:
                # Generate a random number between 1 and 9
                num = random.randint(1, 9)
                if unused_in_box(grid, row, col, num):
                    break
            grid.terrain[row + i][col + j].occupant = num
            grid.terrain[row + i][col + j].base=True
            grid.update()


# Check if it's safe to put num in the cell (i, j)
# Ensure num is not used in row, column, or box
def check_if_safe(grid, i, j, num):
    return (not grid.check_ligne(i, num) and 
            not grid.check_colone(j, num) and 
            not grid.check_subdiv( subdiv([i,j,0])[2], num))

# Fill the diagonal 3x3 matrices
# The diagonal blocks are filled to simplify the process
def fill_diagonal(grid):
    for i in range(0, 9, 3):

        # Fill each 3x3 subgrid diagonally
        fill_box(grid, i, i)


# Fill remaining blocks in the grid
# Recursively fill the remaining cells with valid numbers
def fil_remaining(grid, i, j):
    # If we've reached the end of the grid
    if i == 9:
        return True
    
    # Move to next row when current row is finished
    if j == 9:
        return fil_remaining(grid, i + 1, 0)
    
    # Skip if cell is already filled
    if grid.terrain[i][j].occupant != 0:
        return fil_remaining(grid, i, j + 1)
    
    # Try numbers 1-9 in current cell
    for num in range(1, 10):
        if check_if_safe(grid, i, j, num):
            grid.terrain[i][j].occupant = num
            grid.terrain[i][j].base=True
            grid.update()
            if fil_remaining(grid, i, j + 1):
                return True
            grid.terrain[i][j].occupant = 0 
    
    return False

# Remove K digits randomly from the grid
# This will create a Sudoku puzzle by removing digits
def remove_k_digits(grid, k):
    while k > 0:
        
        # Pick a random cell
        cell_id = random.randint(0, 80)

        # Get the row index
        i = cell_id // 9

        # Get the column index
        j = cell_id % 9

        # Remove the digit if the cell is not already empty
        if grid[i][j].occupant  != 0:
            # Empty the cell
            grid[i][j].occupant = 0
            grid[i][j].base= False
            # Decrease the count of digits to remove
            k -= 1

# Generate a Sudoku grid with K empty cells
def sudoku_generator(k):
    
    # Initialize an empty 9x9 grid
    grid=Jeu()
    # Fill the diagonal 3x3 matrices
    fill_diagonal(grid)
    # Fill the remaining blocks in the grid
    fil_remaining(grid, 0, 0)
    # Remove K digits randomly to create the puzzle
    remove_k_digits(grid.terrain, k)

    return grid

if __name__ == "__main__":
    
    # Seed the random number generator
    # random.seed()

    # Set the number of empty cells
    k = 64
    sudoku = sudoku_generator(k)

    # Print the generated Sudoku puzzle
    print(sudoku)