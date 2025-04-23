from Board import Board
from Box import Box
def sub_div(pointer):
    row_group = pointer[0] // 3
    col_group = pointer[1] // 3
    pointer[2] = row_group * 3 + col_group + 1
    return pointer
def avancer(pointer: list, sens: int, box: Box, base=False):
    def move_forward():
        pointer[1] += 1
        if pointer[1] == 9:
            pointer[1] = 0
            pointer[0] += 1
        return sub_div(pointer)

    def move_backward():
        pointer[1] -= 1
        if pointer[1] == -1:
            pointer[1] = 8
            pointer[0] -= 1
        return sub_div(pointer)

    if base:
        pointer = move_forward() if sens == 1 else move_backward()
        return

    if sens == 1:
        box.arrival(box.possible[0])
        box.possible.pop(0)
        pointer = move_forward()
    else:
        box.leave()
        pointer = move_backward()

def resoudre(j:Board):
    temp=j
    pointeur=[0,0,1]
    '''le pointeur est défini par les coordonnées et la sous division'''
    sens=1
    '''on vérifie si la grille est réalisable'''
    
    while True :
        if j.terrain[pointeur[0]][pointeur[1]].base==False:
            for _ in range (1):
                if j.terrain[pointeur[0]][pointeur[1]].possible==[]:
                    if sens == -1:
                        break
                    else:
                        j.terrain[pointeur[0]][pointeur[1]].possible= [i for i in range(1,len(j.terrain)+1)]
                while j.terrain[pointeur[0]][pointeur[1]].possible!=[]:
                    i=j.terrain[pointeur[0]][pointeur[1]].possible[0]
                    print(pointeur)
                    if not j.check_ligne(pointeur[0],i) and not j.check_column(pointeur[1],i) and not j.check_subdiv(pointeur[2],i) :
                        sens=1
                        break
                    else:
                        j.terrain[pointeur[0]][pointeur[1]].possible.pop(0)
                        sens=-1
        else:
            j.terrain[pointeur[0]][pointeur[1]].possible= [i for i in range(1,10) if i not in [j.terrain[pointeur[0]][pointeur[1]].occupant]]
        j.update(pointeur[0],pointeur[1])
        avancer(pointeur,sens,j.terrain[pointeur[0]][pointeur[1]],True)
        print(pointeur)
        if pointeur==[9,0,10]:
            return temp,j
def resoudre(j: Board):
    temp = j
    pointeur = [0, 0, 1]  # [row, col, sub]
    sens = 1

    def reset_possibilities():
        return list(range(1, len(j.terrain) + 1))

    def is_valid(j, row, col, sub, value):
        return (
            not j.check_ligne(row, value)
            and not j.check_column(col, value)
            and not j.check_subdiv(sub, value)
        )

    def fill_base_cell(cell):
        cell.possible = [i for i in range(1, 10) if i != cell.occupant]

    def try_possibilities(cell, row, col, sub):
        nonlocal sens
        if not cell.possible:
            if sens == -1:
                return
            cell.possible = reset_possibilities()
        while cell.possible:
            value = cell.possible[0]
            print(pointeur)
            if is_valid(j, row, col, sub, value):
                sens = 1
                return
            cell.possible.pop(0)
            sens = -1

    while True:
        row, col, sub = pointeur
        cell = j.terrain[row][col]

        if not cell.base:
            try_possibilities(cell, row, col, sub)
        else:
            fill_base_cell(cell)

        j.update(row, col)
        avancer(pointeur, sens, cell, True)
        print(pointeur)

        if pointeur == [9, 0, 10]:
            return temp, j



        
if __name__=="__main__":
    Game1=Board()
    Game1.set_terrain([
        [0,0,0,0,0,0,6,0,2],
        [0,6,2,8,7,0,0,3,4],
        [3,4,1,9,0,0,0,7,8],
        [0,9,6,7,2,8,4,0,3],
        [0,0,4,6,0,3,0,1,0],
        [0,5,0,0,0,0,7,0,6],
        [7,0,9,1,0,6,2,0,5],
        [0,0,0,0,3,7,0,0,1],
        [0,1,5,2,8,9,0,6,0]
    ])
    Game2=Board()
    Game2.set_terrain([
        [0,0,1,0,0,0,0,0,0],
        [8,0,0,0,0,0,0,9,4],
        [0,9,0,0,0,0,0,0,0],
        [0,0,8,0,0,4,0,7,0],
        [0,0,0,0,0,1,0,0,0],
        [0,0,0,5,0,0,3,0,2],
        [0,0,5,1,0,2,0,0,0],
        [4,3,0,0,0,9,0,0,0],
        [0,1,0,0,0,3,0,0,0]
    ])
    Game3=Board()
    Game3.set_terrain([
        [8,7,5,3,6,2,9,1,4],
        [0,0,3,0,0,0,0,0,0],
        [0,0,0,0,0,5,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [2,0,0,5,0,0,0,9,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,7,0,0],
        [0,3,0,0,5,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]
    ])
    Game4=Board()
    Game4.set_terrain([
        [9,4,0,0,3,8,0,0,0],
        [0,0,0,0,0,0,9,6,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,3],
        [1,5,0,0,0,0,0,0,0],
        [0,0,0,0,5,4,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,7,2,0],
        [4,0,0,0,0,3,5,0,0]
    ])

    # print(Game3)
    print(Game1.is_solvable())
    print(resoudre(Game1))
    # print(Game3)