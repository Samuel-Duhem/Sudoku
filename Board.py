from Box import Box
class Board:
    def __init__(self):
        '''define a Board filled with boxes, the solution if there is one '''
        m=[[Box(0) for _ in range(9)]for _ in range(9)]
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
        self.soluce=None

    def get_subdiv(self,i,j):
        '''return the subdiv of 2 coordinates '''
        row = i // 3
        col = j // 3
        return row*3 + col+1
    def check_ligne(self,l,x):
        '''A function that check if there is an occuration of a number in a ligne'''
        temp=[]
        for i in range(len(self.terrain)):
            temp.append(self.terrain[l][i].occupant)
        return x in temp
    def check_column(self,c,x):
        '''A function that check if there is an occuration of a number in a column'''
        temp=[]
        for i in range(len(self.terrain)):
            temp.append(self.terrain[i][c].occupant)
        return x in temp
    def check_subdiv(self, n:int, x:int):
        '''A function that check if there is an occuration of a number in a subdiv'''
        for ligne in self.subdiv[n]:
            for box in ligne:
                if x==box.occupant: 
                    return True
        return False
    def update(self):
        '''update the subdivision when we change a number'''
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

    def set_terrain(self,matrice):
        '''define the grid from a matrix'''
        for i in range(len(matrice)):
            for j in range(len(matrice)):
                if matrice[i][j]!=0:
                    base=True
                else:
                    base=False
                self.terrain[i][j]=Box(occupant=matrice[i][j],base=base)
        self.update()

    def is_solvable(self):
        '''check if the grid is solvable'''
        for i in range(9):
            for j in range(9) :
                if self.terrain[i][j].base:
                    if self.check_ligne(i, self.terrain[i][j].occupant) or  self.check_column(j, self.terrain[i][j].occupant) or self.check_subdiv(self.get_subdiv(i, j), self.terrain[i][j].occupant):
                        return False
        return True
    def __str__(self):
        '''print the grid after line with different colors'''
        total= (' ___________________________________ '+'\n')
        for ligne in self.terrain:
            for box in ligne:
                if box.free():
                    total+=('|   ')
                else:
                    total+=(f"| \033[{99 + int(box.occupant)}m{box.occupant}\033[0m ")
            total+=('|'+'\n')
            total+=('|___|___|___|___|___|___|___|___|___|'+'\n')
        return total
