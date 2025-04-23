class Box:
    '''
        - Class that define a box with the possibles occupant 
        wich, for the soduku or all positive figures.\n
        We also define is the number within the box is here from scratch
    '''
    def __init__(self,occupant=0,base=False):
        self.possible=[i for i in range(1,10)]
        self.occupant=occupant
        self.base=base

    def free(self):
        ''' 
            - We check if the box is empty\n
            - Return True if it is
        '''
        return self.occupant ==0
    

    def leave(self):
        '''
            - Make the box empty\n
            - Return nothing
        '''
        self.occupant=0
    

    def arrival(self,n:int):
        ''' 
            - Put a number into the box
            - Return nothing
        '''
        self.occupant=n
    

    def __str__(self):
        return str(self.occupant)
