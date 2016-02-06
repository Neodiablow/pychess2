#! /usr/bin/env python3
import string

alphabet=string.ascii_uppercase[0:8] #string used for chess board
lb = alphabet.index("B")
ub = alphabet.index("G")

class Ghost():
    """The reaper queen aka the Reaper"""
    def __init__(self,c,a):
        self.piece="Ghost"
        self.color=bool(c)
        self.army=str(a)
   
    def moves(self,x,y):
        listR=[]
        for xValue in range(alphabet.index('A'),alphabet.index('H')+1):
             for yValue in range (1,9):
                listR+=[(alphabet[xValue],yValue)]
        
        listR.remove((x,y))
        return listR
