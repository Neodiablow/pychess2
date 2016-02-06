#! /usr/bin/env python3
import string
from Core.Pieces.abs_pawn import AbsPawn

alphabet=string.ascii_uppercase[0:8] #string used for chess board
lb = alphabet.index("B")
ub = alphabet.index("G")

class Pawn(AbsPawn):
    def moves(self,x,y):
        return self.pawnMoves(x,y)

