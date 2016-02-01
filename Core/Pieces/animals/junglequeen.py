#! /usr/bin/env python3
import string
from Core.Pieces.abs_rook import AbsRook
from Core.Pieces.abs_knight import AbsKnight

alphabet=string.ascii_uppercase[0:8] #string used for chess board
lb = alphabet.index("B")
ub = alphabet.index("G")

class JungleQueen(AbsRook,AbsKnight):
    """A piece of chess"""
    def __init__(self,c,a):
        self.piece="Queen"
        self.color=bool(c)
        self.army=str(a)
#    
    def moves(self,x,y):
#    """Returns Valid moves to the model"""
#        listV=[]
#        listH=[]
#        listD=[]
#        """Rook moves, vertical line, + horizontal line
#        add the tuple to lists(H&V) declared above"""
#        for yValue in range(1,9):
#           listV+=[(x,yValue)] 
#        for xValue in range(alphabet.index('A'),alphabet.index('H')+1):
#           listH+=[(alphabet[xValue],y)]
#
#        """Bishop moves, diagonal lines, both directions
#        add the tuple to listD declared above
#        needs two loops to work, 
#        one to find "increasing coordinates" 
#        one to find "decreasing coordinates" """
#        xValue=alphabet.index(x)
#        yValue=y
#        while xValue <= alphabet.index("H") and yValue < 8:
#            xValue+=1
#            yValue+=1
#            listD+=[(alphabet[xValue],yValue)]
#        xValue=alphabet.index(x)
#        yValue=y
#        while xValue >= alphabet.index("A") and yValue > 1:
#            xValue-=1
#            yValue-=1
#            listD+=[(alphabet[xValue],yValue)]
#
#        """Remove moves which are not moves"""
#        listH.remove((x,y))
#        listV.remove((x,y))
#
#        return listH+listV+listD
        return self.rookMoves(x,y) + self.knightMoves(x,y)

