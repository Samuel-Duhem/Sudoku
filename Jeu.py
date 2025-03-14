from Case import *
class Jeu:
    def __init__(self):
        m=[[case(0) for i in range(9)]for j in range(9)]
        self.terrain=m
        self.subdiv={

            1:[self.terrain[0][0:3],self.terrain[1][0:3],self.terrain[2][0:3]],
            2:[self.terrain[0][3:6],self.terrain[1][3:6],self.terrain[2][3:6]],
            3:[self.terrain[0][6:9],self.terrain[1][6:9],self.terrain[2][6:9]],
            4:[self.terrain[3][0:3],self.terrain[4][0:3],self.terrain[5][0:3]],
            5:[self.terrain[3][3:6],self.terrain[4][3:6],self.terrain[5][3:6]],
            6:[self.terrain[3][6:9],self.terrain[4][6:9],self.terrain[5][6:9]],
            7:[self.terrain[6][0:3],self.terrain[7][0:3],self.terrain[8][0:3]],
            8:[self.terrain[6][3:6],self.terrain[7][3:6],self.terrain[8][3:6]],
            9:[self.terrain[6][6:9],self.terrain[7][6:9],self.terrain[8][6:9]]

        }


    def CheckLigne(self,l,x):
        temp=[]
        for i in range(len(self.terrain)):
            temp.append(self.terrain[l][i].occupant)
        return x in temp
    def CheckColone(self,c,x):
        temp=[]
        for i in range(len(self.terrain)):
            temp.append(self.terrain[i][c].occupant)
        return x in temp
    def CheckSubDiv(self, n:int, x:int):
        for ligne in self.subdiv[n]:
            for case in ligne:
                if x==case.occupant: 
                    return True
        return False
    def update(self):
        self.subdiv={

            1:[self.terrain[0][0:3],self.terrain[1][0:3],self.terrain[2][0:3]],
            2:[self.terrain[0][3:6],self.terrain[1][3:6],self.terrain[2][3:6]],
            3:[self.terrain[0][6:9],self.terrain[1][6:9],self.terrain[2][6:9]],
            4:[self.terrain[3][0:3],self.terrain[4][0:3],self.terrain[5][0:3]],
            5:[self.terrain[3][3:6],self.terrain[4][3:6],self.terrain[5][3:6]],
            6:[self.terrain[3][6:9],self.terrain[4][6:9],self.terrain[5][6:9]],
            7:[self.terrain[6][0:3],self.terrain[7][0:3],self.terrain[8][0:3]],
            8:[self.terrain[6][3:6],self.terrain[7][3:6],self.terrain[8][3:6]],
            9:[self.terrain[6][6:9],self.terrain[7][6:9],self.terrain[8][6:9]]

        }

    def SetTerrain(self,matrice):
        for i in range(len(matrice)):
            for j in range(len(matrice)):
                if matrice[i][j]!=0:
                    base=True
                else:
                    base=False
                self.terrain[i][j]=case(occupant=matrice[i][j],base=base)
        self.update()
    
    def fini(self):
        for i in range(len(self.terrain)-1):
            for j in range(len(self.terrain)-1):
                if self.terrain[i][j].libre():
                    return False
        return True
    def __str__(self):
        total= (' ___________________________________ '+'\n')
        for ligne in self.terrain:
            for case in ligne:
                if case.libre():
                    total+=('|   ')
                elif not case.libre():
                    total+=(f"| \033[{99 + int(case.occupant)}m{case.occupant}\033[0m ")
            total+=('|'+'\n')
            total+=('|___|___|___|___|___|___|___|___|___|'+'\n')
        return total
    '''afficher la grille ligne par ligne'''