from Jeu import *
from Case import *
def subDiv(Pointeur):
    if Pointeur[0] in [0,1,2]:
        if Pointeur[1] in [0,1,2]:
            Pointeur[2]=1
        if  Pointeur[1] in [3,4,5]:
            Pointeur[2]=2
        if  Pointeur[1] in [6,7,8]:
            Pointeur[2]=3
    if Pointeur[0] in [3,4,5]:
        if Pointeur[1] in [0,1,2]:
            Pointeur[2]=4
        if  Pointeur[1] in [3,4,5]:
            Pointeur[2]=5
        if  Pointeur[1] in [6,7,8]:
            Pointeur[2]=6
    if Pointeur[0] in [6,7,8]:
        if Pointeur[1] in [0,1,2]:
            Pointeur[2]=7
        if  Pointeur[1] in [3,4,5]:
            Pointeur[2]=8
        if  Pointeur[1] in [6,7,8]:
            Pointeur[2]=9
    return Pointeur
def avancer(Pointeur:list,sens:int,case:Case,base=False):
    if base:
        if sens==1:
            Pointeur[1]+=1
            if Pointeur[1]==9:
                Pointeur[1]=0
                Pointeur[0]+=1
            Pointeur=subDiv(Pointeur)
            return
        else:
            Pointeur[1]-=1
            if Pointeur[1]==-1:
                Pointeur[1]=8
                Pointeur[0]-=1
            Pointeur=subDiv(Pointeur)
            return
    if sens==1:
        case.arrivee(case.possible[0])
        case.possible.pop(0)
        Pointeur[1]+=1
        if Pointeur[1]==9:
            Pointeur[1]=0
            Pointeur[0]+=1
        Pointeur=subDiv(Pointeur)
    else:
        case.depart()
        Pointeur[1]-=1
        if Pointeur[1]==-1:
            Pointeur[1]=8
            Pointeur[0]-=1
        Pointeur=subDiv(Pointeur)
def resoudre(j:Jeu):
    temp=j
    Pointeur=[0,0,1]
    '''le pointeur est défini par les coordonnées et la sous division'''
    remov=False
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
            for a in range (1):
                if j.terrain[Pointeur[0]][Pointeur[1]].possible==[]:
                    if sens == -1:
                        break
                    else:
                        j.terrain[Pointeur[0]][Pointeur[1]].possible= [i for i in range(1,len(j.terrain)+1)]
                while j.terrain[Pointeur[0]][Pointeur[1]].possible!=[]:
                    remov==False
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