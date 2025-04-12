class Box:
    '''Class that define a box with the possibles occupant 
    wich, for the soduku or all positive figures.
    We also define is the number within the box is here from scratch'''
    def __init__(self,occupant=0,base=False):
        self.possible=[i for i in range(1,10)]
        self.occupant=occupant
        self.base=base

    def free(self):
        return self.occupant ==0
    ''' we check if the box is empty'''

    def leave(self):
        self.occupant=0
    '''make the box empty'''

    def arrival(self,n):
        self.occupant=n
    ''' put a number into the box'''

    def __str__(self):
        return str(self.occupant)
    '''print the box'''
