from Box import Box
class Board:
    '''
        - Define a Board with the terrain, a square matix a 9X9 Boxes.
        We can acces each subdiv individually with the number of the subdiv,
        going from 1 to 9. If the grid as been randomly generated, the solution is stored
    '''
    def __init__(self):
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
        
    def get_subdiv(self,i:int,j:int,pos=False):
        '''
            - Acces the subdiv of the i;j box 
            - Return the subdiv of 2 coordinates.
            If pos is enable, also return the position inside the subdiv    
        '''
        row = i // 3
        col = j // 3
        if pos==True:
            return row*3 + col+1, i-row*3,j-col*3
        return row*3 + col+1
        
    def check_ligne(self,l:int,x:int):
        '''
            - A function that check if there is an occuration of a number in a ligne
            - Return True if there is x in the l ligne
        '''
        temp=[]
        for i in range(len(self.terrain)):
            temp.append(self.terrain[l][i].occupant)
        return x in temp
    
    def check_column(self,c:int,x:int):
        '''
            - A function that check if there is an occuration of a number in a column
            - Return True if there is x in the c column
        '''
        temp=[]
        for i in range(len(self.terrain)):
            temp.append(self.terrain[i][c].occupant)
        return x in temp
    
    def check_subdiv(self, n:int, x:int):
        '''
            - A function that check if there is an occuration of a number in a subdiv
            - Return True if there is x in the n subdiv
        '''        
        for ligne in self.subdiv[n]:
            for box in ligne:
                if x==box.occupant: 
                    return True
        return False
    
    def is_safe(self, i:int, j:int, num:int):
        '''
            - Utilize the three previous function to make sure the box is ready to take num
            - Return True if the i;j box is safe for num 
        '''
        return (not self.check_ligne(i, num) and 
            not self.check_column(j, num) and 
            not self.check_subdiv( self.get_subdiv(i,j), num))
        
    def update(self,i:int,j:int):
        '''
            - Redefine the subdiv dictionary for the i;j box to match the terrain
            - Return nothing
        '''
        temp=self.get_subdiv(i,j,True)
        (self.subdiv[temp[0]])[temp[1]][temp[2]]=self.terrain[i][j]
        
    def set_terrain(self,matrix:list[list[Box]]):
        '''
            - Define the grid from a matrix
            - Does not return anything
        '''
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if matrix[i][j]!=0:
                    base=True
                else:
                    base=False
                self.terrain[i][j]=Box(occupant=matrix[i][j],base=base)
                self.update(i,j)
        
    def is_solvable(self):
        '''
            - Check if the grid is solvable
            - Return True if the board is solvable
        '''
        for i in range(9):
            for j in range(9):
                if self.terrain[i][j].base:
                    # we empty the box to check if there is another one of the occupant
                    temp=self.terrain[i][j]
                    self.terrain[i][j]=Box()
                    self.update(i,j)
                    if not self.is_safe(i,j,temp.occupant):
                        self.terrain[i][j]=temp
                        return False
                    self.terrain[i][j]=temp
        return True
    
    def __str__(self):
        total= (' ___________________________________ '+'\n')
        for ligne in self.terrain:
            for box in ligne:
                if box.free():
                    total+=('|   ')
                else:
                    # show colors in the terminal
                    total+=(f"| \033[{99 + int(str(box))}m{str(box)}\033[0m ")
            total+=('|'+'\n')
            total+=('|___|___|___|___|___|___|___|___|___|'+'\n')
        return total
    
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
        [0,6,0,0,3,7,0,0,1],
        [0,1,5,2,8,9,0,6,0]
    ])
    print(Game1.is_solvable())
    print(Game1)
    print(Game1.subdiv[1])
    print(Game1.get_subdiv(3,3,True))