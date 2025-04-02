
class case:
'''Class that define a box with the possibles occupant 
wich, for the soduku or all positive figures'''
    def __init__(self,occupant=0,base=False):
        self.possible=[i for i in range(1,10)]
        self.occupant=occupant
        self.base=base
    '''we initialize the box with its terrain and its occupant. 
    base allows you to know if the occupant has been there from
    the start or if he is there temporarily'''

    def libre(self):
        return self.occupant ==0
    ''' we check if the box is empty'''

    def depart (self):
        self.occupant=0
    '''make the box empty'''

    def arrivee (self,n):
        self.occupant=n
    ''' put a number into the box'''

    def __str__(self):
        return str(self.occupant)
    '''print the box'''
