#! /usr/bin/env python3
import string
alphabet=string.ascii_uppercase[0:8] #string used for chess board
lb = alphabet.index("B")
ub = alphabet.index("G")

class Pawn:
    """Most basic piece of chess """
    def __init__(self,c,a):
#        self.name=("pawn"+row+col).upper() #useless
        self.piece="Pawn"
#        self.position=str(row+col).upper()
        self.color=bool(c)
        self.army=str(a)
    
#    def sayMyName(self): #useless
#        print(self.name)

#    def displayPosition(self):
#        print(self.piece,self.color,self.position)
    
#    def select(self):
#        self.displayPosition()

    def moves(self,x,y):
        """Returns Valid moves to the model"""
        if alphabet.index(x) in range(lb,ub):
            if self.color:
                return [(alphabet[alphabet.index(x)],y+1),(alphabet[alphabet.index(x)],y+2),(alphabet[alphabet.index(x)+1],y+1),(alphabet[alphabet.index(x)-1],y+1)]
            else:
                return [(alphabet[alphabet.index(x)],y-1),(alphabet[alphabet.index(x)],y-2),(alphabet[alphabet.index(x)+1],y-1),(alphabet[alphabet.index(x)-1],y-1)]
        elif alphabet.index(x) == alphabet.index("A"):
            if self.color:
                return [(alphabet[alphabet.index(x)],y+1),(alphabet[alphabet.index(x)],y+2),(alphabet[alphabet.index(x)+1],y+1)]
            else:
                return [(alphabet[alphabet.index(x)],y-1),(alphabet[alphabet.index(x)],y-2),(alphabet[alphabet.index(x)+1],y-1)]
            
        elif alphabet.index(x) == alphabet.index("H"):
            if self.color:
                return [(alphabet[alphabet.index(x)],y+1),(alphabet[alphabet.index(x)],y+2),(alphabet[alphabet.index(x)-1],y+1)]
            else:
                return [(alphabet[alphabet.index(x)],y-1),(alphabet[alphabet.index(x)],y-2),(alphabet[alphabet.index(x)-1],y-1)]

        
#a=Pawn("2","a",True,"Classic")
#a.sayMyName()
#a.select()
pawnW=Pawn(True,"classic")
pawnB=Pawn(False,"classic")
print("PawnW :",pawnW.moves("B",4))
print("PawnB :",pawnW.moves("E",4))
print("PawnW :",pawnW.moves("A",2))
print("PawnB :",pawnW.moves("A",3))
print("PawnW :",pawnW.moves("H",4))
print("PawnB :",pawnW.moves("H",4))
print(alphabet)
