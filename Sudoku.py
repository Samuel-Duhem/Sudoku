from Jeu import Jeu
from Case import Case
def sub_div(pointeur):
    row_group = pointeur[0] // 3
    col_group = pointeur[1] // 3
    pointeur[2] = row_group * 3 + col_group + 1
    return pointeur
def avancer(pointeur: list, sens: int, case: Case, base=False):
    def move_forward():
        pointeur[1] += 1
        if pointeur[1] == 9:
            pointeur[1] = 0
            pointeur[0] += 1
        return sub_div(pointeur)

    def move_backward():
        pointeur[1] -= 1
        if pointeur[1] == -1:
            pointeur[1] = 8
            pointeur[0] -= 1
        return sub_div(pointeur)

    if base:
        pointeur = move_forward() if sens == 1 else move_backward()
        return

    if sens == 1:
        case.arrivee(case.possible[0])
        case.possible.pop(0)
        pointeur = move_forward()
    else:
        case.depart()
        pointeur = move_backward()
def resoudre(j:Jeu):
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
                    if not j.check_ligne(pointeur[0],i) and not j.check_colone(pointeur[1],i) and not j.check_subdiv(pointeur[2],i) :
                        sens=1
                        break
                    else:
                        j.terrain[pointeur[0]][pointeur[1]].possible.pop(0)
                        sens=-1
            avancer(pointeur,sens,j.terrain[pointeur[0]][pointeur[1]])
            j.update()
        else:
            j.terrain[pointeur[0]][pointeur[1]].possible= [i for i in range(1,10) if i not in [j.terrain[pointeur[0]][pointeur[1]].occupant]]
            avancer(pointeur,sens,j.terrain[pointeur[0]][pointeur[1]],True)
            j.update()
        if pointeur==[9,0,9]:
            return temp,j
    

if __name__=="__main__":
    iJeu1=Jeu()
    iJeu1.set_terrain([
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
    iJeu2=Jeu()
    iJeu2.set_terrain([
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
    iJeu3=Jeu()
    iJeu3.set_terrain([
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
    iJeu4=Jeu()
    iJeu4.set_terrain([
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

    # print(iJeu3)
    print(resoudre(iJeu3)[1])
    # print(iJeu3)