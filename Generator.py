from Board import Board
from Sudoku import sub_div
import random as r

def fill_box(grid:Board, row:int, col:int):
    '''

    '''
    sub=grid.get_subdiv(row,col)
    for i in range(3):
        for j in range(3):
            while True:
                num = r.randint(1, 9)
                if not grid.check_subdiv( sub, num):
                    break
            grid.terrain[row + i][col + j].occupant = num
            grid.terrain[row + i][col + j].base=True
            grid.update(i,j)


def fill_diagonal(grid:Board):
    '''
        - Function that fill the 1,5 and 9 subdiv.
        - Doesn't return anything, juste modify the values of the Board
    '''
    for i in range(0, 9, 3):
        print(i,i)
        # Fill each 3x3 subgrid diagonally
        fill_box(grid, i, i)

def fil_remaining(grid:Board, i:int, j:int):
    '''
        - Recursive function wich fill the 2,3,4,6,7 and 8 subdiv. i and j are the starting coordonates
        - Return a bool for the recursivity but is used to modify the differents values of grid
    '''
    
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
        if grid.is_safe( i, j, num):
            grid.terrain[i][j].occupant = num
            grid.terrain[i][j].base=True
            grid.update(i,j)
            if fil_remaining(grid, i, j + 1):
                return True
            grid.terrain[i][j].occupant = 0 
    
    return False

def remove_k_digits(grid:Board, k:int):
    '''
        - Take a borad and remove k digits from it
        - Does not return anything
    '''
    while k > 0:
        cell_id = r.randint(0, 80)
        i = cell_id // 9
        j = cell_id % 9
        if grid.terrain[i][j].occupant  != 0:
            grid.terrain[i][j].occupant = 0
            grid.terrain[i][j].base= False
            k -= 1

def sudoku_generator(k:int):
    ''' 
        - Generate a Sudoku with k empty cells
        - Return the Board
    '''
    grid=Board()
    fill_diagonal(grid)
    fil_remaining(grid, 0, 0)
    grid.save_soluce(grid,'Soluce.pkl')
    
    remove_k_digits(grid, k)

    return grid

if __name__ == "__main__":
    k = 30
    sudoku = sudoku_generator(k)
    print(sudoku)
    print(sudoku.get_soluce())
