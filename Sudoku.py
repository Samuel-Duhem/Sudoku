from Jeu import Jeu
from Case import Case

def subdiv(pointeur):
    subdivisions = {
        (0, 0): 1, (0, 1): 1, (0, 2): 1, (1, 0): 1, (1, 1): 1, (1, 2): 1, (2, 0): 1, (2, 1): 1, (2, 2): 1,
        (0, 3): 2, (0, 4): 2, (0, 5): 2, (1, 3): 2, (1, 4): 2, (1, 5): 2, (2, 3): 2, (2, 4): 2, (2, 5): 2,
        (0, 6): 3, (0, 7): 3, (0, 8): 3, (1, 6): 3, (1, 7): 3, (1, 8): 3, (2, 6): 3, (2, 7): 3, (2, 8): 3,
        (3, 0): 4, (3, 1): 4, (3, 2): 4, (4, 0): 4, (4, 1): 4, (4, 2): 4, (5, 0): 4, (5, 1): 4, (5, 2): 4,
        (3, 3): 5, (3, 4): 5, (3, 5): 5, (4, 3): 5, (4, 4): 5, (4, 5): 5, (5, 3): 5, (5, 4): 5, (5, 5): 5,
        (3, 6): 6, (3, 7): 6, (3, 8): 6, (4, 6): 6, (4, 7): 6, (4, 8): 6, (5, 6): 6, (5, 7): 6, (5, 8): 6,
        (6, 0): 7, (6, 1): 7, (6, 2): 7, (7, 0): 7, (7, 1): 7, (7, 2): 7, (8, 0): 7, (8, 1): 7, (8, 2): 7,
        (6, 3): 8, (6, 4): 8, (6, 5): 8, (7, 3): 8, (7, 4): 8, (7, 5): 8, (8, 3): 8, (8, 4): 8, (8, 5): 8,
        (6, 6): 9, (6, 7): 9, (6, 8): 9, (7, 6): 9, (7, 7): 9, (7, 8): 9, (8, 6): 9, (8, 7): 9, (8, 8): 9,
    }
    pointeur[2] = subdivisions[(pointeur[0], pointeur[1])]
    return pointeur
def avancer(pointeur: list, sens: int, case: Case, base=False):
    if base:
        avancer_base(pointeur, sens)
    else:
        avancer_non_base(pointeur, sens, case)

def avancer_base(pointeur: list, sens: int):
    if sens == 1:
        pointeur[1] += 1
        if pointeur[1] == 9:
            pointeur[1] = 0
            pointeur[0] += 1
    else:
        pointeur[1] -= 1
        if pointeur[1] == -1:
            pointeur[1] = 8
            pointeur[0] -= 1
    pointeur = subdiv(pointeur)

def avancer_non_base(pointeur: list, sens: int, case: Case):
    if sens == 1:
        case.arrivee(case.possible[0])
        case.possible.pop(0)
        pointeur[1] += 1
        if pointeur[1] == 9:
            pointeur[1] = 0
            pointeur[0] += 1
    else:
        case.depart()
def resoudre(j:Jeu):
    temp=j
    Pointeur=[0,0,1]
    '''le pointeur est défini par les coordonnées et la sous division'''
    sens=1
    # for k in range(64):
    '''on vérifie si la grille est réalisable'''
    # for i in range(len(j.terrain)):
    #     for ii in range(len(j.terrain[i])):
    #         local=j.terrain[i][ii].occupant
    #         if j.CheckLigne(Pointeur[0],local) or j.CheckColone(Pointeur[1],local) or j.CheckSubDiv(Pointeur[2],local) :
    #             return "Grille imopossible"
    
    while True :
        if j.terrain[Pointeur[0]][Pointeur[1]].base==False:
            for _ in range (1):
                if j.terrain[Pointeur[0]][Pointeur[1]].possible==[]:
                    if sens == -1:
                        break
                    else:
                        j.terrain[Pointeur[0]][Pointeur[1]].possible= [i for i in range(1,len(j.terrain)+1)]
                while j.terrain[Pointeur[0]][Pointeur[1]].possible!=[]:
                    i=j.terrain[Pointeur[0]][Pointeur[1]].possible[0]
                    if not j.check_ligne(Pointeur[0],i) and not j.check_colone(Pointeur[1],i) and not j.check_subdiv(Pointeur[2],i) :
                        sens=1
                        break
                    else:
                        j.terrain[Pointeur[0]][Pointeur[1]].possible.pop(0)
                        sens=-1
            avancer(Pointeur,sens,j.terrain[Pointeur[0]][Pointeur[1]])
            j.update()
        else:
            j.terrain[Pointeur[0]][Pointeur[1]].possible= [i for i in range(1,10) if i not in [j.terrain[Pointeur[0]][Pointeur[1]].occupant]]
            avancer(Pointeur,sens,j.terrain[Pointeur[0]][Pointeur[1]],True)
            j.update()
        if Pointeur==[9,0,9]:
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