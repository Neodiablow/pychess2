#! /usr/bin/env python3
import string
from Core.Pieces.abs_king import AbsKing
alphabet=string.ascii_uppercase[0:8] #string used for chess board
lb = alphabet.index("B")
ub = alphabet.index("G")

class King(AbsKing):
    """Most important piece of chess"""
    def __init__(self,c,a):
        self.piece="King"
        self.color=bool(c)
        self.army=str(a)
    
    def moves(self,x,y):
        return self.kingMoves(x,y)
    
    def smallCastle(self):
        if self.color and self.army == "Classic":
            return ["G",1]
        elif self.army == "Classic":
            return ["G",8]
        else :
            return []
    def bigCastle(self):
        if self.color and self.army == "Classic":
            return ["B",1]
        elif self.army == "Classic":
            return ["B",8]
        else :
            return []

