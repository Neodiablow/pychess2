#! /usr/bin/env python3
import string
from Core.Pieces.abs_knight import AbsKnight
alphabet=string.ascii_uppercase[0:8] #string used for chess board
lb = alphabet.index("B")
ub = alphabet.index("G")

class Knight(AbsKnight):
    def moves(self,x,y):
        return self.knightMoves(x,y)
