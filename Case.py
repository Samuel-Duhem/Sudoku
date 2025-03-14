
class case:

    def __init__(self,occupant=0,base=False):
        self.possible=[i for i in range(1,10)]
        self.occupant=occupant
        self.base=base
    '''on initialise la case avec son terrain et son occupant'''

    def libre(self):
        return self.occupant ==0
    ''' on vérifie si la case est libre'''

    def depart (self):
        self.occupant=0
    '''fait partir le pion de la case'''

    def arrivee (self,n):
        self.occupant=n
    ''' self.occupant pointe vers l'instance de la classe pion dans la case'''

    def __str__(self):
        return str(self.occupant)