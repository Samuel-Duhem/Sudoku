# Python program to generate a valid sudoku 
# with k empty cells
from Jeu import *
from Sudoku import subDiv
import random 

# Returns false if given 3x3 block contains num
# Ensure the number is not used in the box
def unUsedInBox(grid, rowStart, colStart, num):
    for i in range(3):
        for j in range(3):
            if grid.terrain[rowStart + i][colStart + j].occupant == num:
                return False
    return True
# Fill a 3x3 matrix
# Assign valid random numbers to the 3x3 subgrid
def fillBox(grid, row, col):
    for i in range(3):
        for j in range(3):
            while True:
                # Generate a random number between 1 and 9
                num = random.randint(1, 9)
                if unUsedInBox(grid, row, col, num):
                    break
            grid.terrain[row + i][col + j].occupant = num
            grid.terrain[row + i][col + j].base=True
            grid.update()


# Check if it's safe to put num in the cell (i, j)
# Ensure num is not used in row, column, or box
def checkIfSafe(grid, i, j, num):
    return (not grid.CheckLigne(i, num) and 
            not grid.CheckColone(j, num) and 
            not grid.CheckSubDiv( subDiv([i,j,0])[2], num))

# Fill the diagonal 3x3 matrices
# The diagonal blocks are filled to simplify the process
def fillDiagonal(grid):
    for i in range(0, 9, 3):
        
        # Fill each 3x3 subgrid diagonally
        fillBox(grid, i, i)

# Fill remaining blocks in the grid
# Recursively fill the remaining cells with valid numbers
def fillRemaining(grid, i, j):
    # If we've reached the end of the grid
    if i == 9:
        return True
    
    # Move to next row when current row is finished
    if j == 9:
        return fillRemaining(grid, i + 1, 0)
    
    # Skip if cell is already filled
    if grid.terrain[i][j].occupant != 0:
        return fillRemaining(grid, i, j + 1)
    
    # Try numbers 1-9 in current cell
    for num in range(1, 10):
        if checkIfSafe(grid, i, j, num):
            grid.terrain[i][j].occupant = num
            grid.terrain[i][j].base=True
            grid.update()
            if fillRemaining(grid, i, j + 1):
                return True
            grid.terrain[i][j].occupant = 0 
    
    return False

# Remove K digits randomly from the grid
# This will create a Sudoku puzzle by removing digits
def removeKDigits(grid, k):
    while k > 0:
        
        # Pick a random cell
        cellId = random.randint(0, 80)

        # Get the row index
        i = cellId // 9

        # Get the column index
        j = cellId % 9

        # Remove the digit if the cell is not already empty
        if grid[i][j]  != 0:
            # Empty the cell
            grid[i][j].occupant = 0
            grid[i][j].base= False
            # Decrease the count of digits to remove
            k -= 1

# Generate a Sudoku grid with K empty cells
def sudokuGenerator(k):
    
    # Initialize an empty 9x9 grid
    grid=Jeu()
    # Fill the diagonal 3x3 matrices
    fillDiagonal(grid)
    # Fill the remaining blocks in the grid
    fillRemaining(grid, 0, 0)
    # Remove K digits randomly to create the puzzle
    removeKDigits(grid.terrain, k)

    return grid

if __name__ == "__main__":
    
    # Seed the random number generator
    # random.seed()

    # Set the number of empty cells
    k = 64
    sudoku = sudokuGenerator(k)

    # Print the generated Sudoku puzzle
    print(sudoku)