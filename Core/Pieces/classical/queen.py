#! /usr/bin/env python3
import string
from Core.Pieces.abs_rook import AbsRook
from Core.Pieces.abs_bishop import AbsBishop

alphabet=string.ascii_uppercase[0:8] #string used for chess board
lb = alphabet.index("B")
ub = alphabet.index("G")

class Queen(AbsRook,AbsBishop):
    """A piece of chess"""
    def __init__(self,c,a):
        self.piece="Queen"
        self.color=bool(c)
        self.army=str(a)
   
    def moves(self,x,y):
        return self.rookMoves(x,y) + self.bishopMoves(x,y)

