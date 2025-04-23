from Board import Board
from Box import Box
def sub_div(pointer):
    row_group = pointer[0] // 3
    col_group = pointer[1] // 3
    pointer[2] = row_group * 3 + col_group + 1
    return pointer
def avancer(pointer: list, direction: int, box: Box, base=False):
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
        pointer = move_forward() if direction == 1 else move_backward()
        return

    if direction == 1:
        box.arrival(box.possible[0])
        box.possible.pop(0)
        pointer = move_forward()
    else:
        box.leave()
        pointer = move_backward()
def solve(j:Board):
    pointeur=[0,0,1]
    '''le pointeur est défini par les coordonnées et la sous division'''

    direction=1
    soluce=j.get_soluce()
    if soluce!=None:
        return soluce
    '''we check if the grid is solvable( function in the next commit)'''
    
    j.save_soluce(j,filename='Soluce.pkl')
    # print(j.filename)
    game:Board=j.get_soluce()
    print(game)
    while True :
        if game.terrain[pointeur[0]][pointeur[1]].base==False:
            for _ in range (1):
                if game.terrain[pointeur[0]][pointeur[1]].possible==[]:
                    if direction == -1:
                        break
                    else:
                        game.terrain[pointeur[0]][pointeur[1]].possible= [i for i in range(1,len(game.terrain)+1)]
                while game.terrain[pointeur[0]][pointeur[1]].possible!=[]:
                    i=game.terrain[pointeur[0]][pointeur[1]].possible[0]
                    print(pointeur)
                    if not game.check_ligne(pointeur[0],i) and not game.check_column(pointeur[1],i) and not game.check_subdiv(pointeur[2],i) :
                        direction=1
                        break
                    else:
                        game.terrain[pointeur[0]][pointeur[1]].possible.pop(0)
                        direction=-1
            avancer(pointeur,direction,game.terrain[pointeur[0]][pointeur[1]])
            game.update()
        else:
            game.terrain[pointeur[0]][pointeur[1]].possible= [i for i in range(1,10) if i not in [j.terrain[pointeur[0]][pointeur[1]].occupant]]
            avancer(pointeur,direction,game.terrain[pointeur[0]][pointeur[1]],True)
            game.update()
        print(pointeur)
        if pointeur==[9,0,10]:
            j.save_soluce(game,'Soluce.pkl')
            
            return j
        
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

    # print(Board3)
    print(solve(Board1))
    print(Board1)
    print(Board1.get_soluce())
    # print(Board3)