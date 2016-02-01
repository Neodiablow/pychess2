#! /usr/bin/env python3

from Core.Pieces.abs_bishop import AbsBishop
import string
alphabet=string.ascii_uppercase[0:8] #string used for chess board
lb = alphabet.index("B")
ub = alphabet.index("G")

class Bishop(AbsBishop):
    def moves(self,x,y):
        return self.bishopMoves(x,y)
