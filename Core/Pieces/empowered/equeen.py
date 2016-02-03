#! /usr/bin/env python3
import string
from Core.Pieces.abs_king import AbsKing

alphabet=string.ascii_uppercase[0:8] #string used for chess board
lb = alphabet.index("B")
ub = alphabet.index("G")

class EQueen(AbsKing):
    """A piece of chess"""
    def __init__(self,c,a):
        self.piece="EQueen"
        self.color=bool(c)
        self.army=str(a)
   
    def moves(self,x,y):
        return self.kingMoves(x,y) 

#untested
