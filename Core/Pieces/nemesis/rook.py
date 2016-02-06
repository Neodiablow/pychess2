#! /usr/bin/env python3
import string
from Core.Pieces.abs_rook import AbsRook

alphabet=string.ascii_uppercase[0:8] #string used for chess board
lb = alphabet.index("B")
ub = alphabet.index("G")

class Rook(AbsRook):
    def moves(self,x,y):
        return self.rookMoves(x,y)
