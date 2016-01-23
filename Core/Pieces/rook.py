#! /usr/bin/env python3
import string
from abs_rook import AbsRook

alphabet=string.ascii_uppercase[0:8] #string used for chess board
lb = alphabet.index("B")
ub = alphabet.index("G")

class Rook(AbsRook):
    """A piece of chess"""
#    def __init__(self,c,a):
#        self.piece="Rook"
#        self.color=bool(c)
#        self.army=str(a)
    
    def moves(self,x,y):
    #Returns Valid moves to the model
        return self.rookMoves(x,y)
#        listV=[]
#        listH=[]
#        """Rook moves, vertical line, + horizontal line
#        add the tuple to lists(H&V) declared above"""
#        for yValue in range(1,9):
#           listV+=[(x,yValue)] 
#        for xValue in range(alphabet.index('A'),alphabet.index('H')+1):
#           listH+=[(alphabet[xValue],y)]
#
#        """Remove moves which are not moves"""
#        listH.remove((x,y))
#        listV.remove((x,y))
#
#        return listH+listV
rook=Rook(True,"Classical");
print(rook.moves("C",4))
