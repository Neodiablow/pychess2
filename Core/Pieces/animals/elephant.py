#! /usr/bin/env python3
import string

alphabet=string.ascii_uppercase[0:8] #string used for chess board
lb = alphabet.index("B")
ub = alphabet.index("G")

class Elephant():
    """A piece of chess"""
    def __init__(self,c,a):
        self.piece="Elephant"
        self.color=bool(c)
        self.army=str(a)
    
    def moves(self,x,y):
        listV=[]
        listH=[]
        """Rook moves, vertical line, + horizontal line
        add the tuple to lists(H&V) declared above"""
        for yValue in range(y-3,y+4): 
            if yValue >= 1 and yValue <= 9:
                listV+=[(x,yValue)] 

        xValue=alphabet.index(x)
        while xValue > alphabet.index("A") and xValue > alphabet.index(x)-3: 
            xValue-=1
            listH+=[(alphabet[xValue],y)]
        xValue=alphabet.index(x)
        while xValue < alphabet.index("H") and xValue < alphabet.index(x)+3:  
            xValue+=1
            listH+=[(alphabet[xValue],y)]

        return listH+listV

