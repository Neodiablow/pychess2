#! /usr/bin/env python3
import string

alphabet=string.ascii_uppercase[0:8] #string used for chess board
lb = alphabet.index("B")
ub = alphabet.index("G")

class Reaper():
    """The reaper queen aka the Reaper"""
    def __init__(self,c,a):
        self.piece="Reaper"
        self.color=bool(c)
        self.army=str(a)
   
    def moves(self,x,y):
        listR=[]
        """If white all squares but the 8th row
        If black all squares but the 1st row"""
        if self.color:
            for xValue in range(alphabet.index('A'),alphabet.index('H')+1):
                for yValue in range (1,8):
                    listR+=[(alphabet[xValue],yValue)]

        else:
            for xValue in range(alphabet.index('A'),alphabet.index('H')+1):
                for yValue in range (2,9):
                    listR+=[(alphabet[xValue],yValue)]
        
        listR.remove((x,y))
        return listR
