#! /usr/bin/env python3
import string
alphabet=string.ascii_uppercase[0:8] #string used for chess board
lb = alphabet.index("B")
ub = alphabet.index("G")

class AbsKnight:
    """A piece of chess """
    def __init__(self,c,a):
        self.piece="Knight"
        self.color=bool(c)
        self.army=str(a)
    
    def knightMoves(self,x,y):
        """Returns Valid moves to the model"""
        listM=[]                                                    #chronological order
        if alphabet.index("H")>=alphabet.index(x)+1 and y+2 <= 8:   #1 o clock
            listM+=[(alphabet[alphabet.index(x)+1],y+2)]
        if alphabet.index("H")>=alphabet.index(x)+2 and y+1 <= 8:   #2 o clock
            listM+=[(alphabet[alphabet.index(x)+2],y+1)]
        if alphabet.index("H")>=alphabet.index(x)+2 and y-1 >= 1:   #4 o clock
            listM+=[(alphabet[alphabet.index(x)+2],y-1)]
        if alphabet.index("H")>=alphabet.index(x)+1 and y-2 >= 1:   #5 o clock
            listM+=[(alphabet[alphabet.index(x)+1],y-2)]
        if alphabet.index("A")<=alphabet.index(x)-1 and y-2 >= 1:   #7 o clock
            listM+=[(alphabet[alphabet.index(x)-1],y-2)]
        if alphabet.index("A")<=alphabet.index(x)-2 and y-1 >= 1:   #8 o clock
            listM+=[(alphabet[alphabet.index(x)-2],y-1)]
        if alphabet.index("A")<=alphabet.index(x)-2 and y+1 <= 8:   #10 o clock
            listM+=[(alphabet[alphabet.index(x)-2],y+1)]
        if alphabet.index("A")<=alphabet.index(x)-1 and y+2 <= 8:   #11 o clock
            listM+=[(alphabet[alphabet.index(x)-1],y+2)]

        return listM
