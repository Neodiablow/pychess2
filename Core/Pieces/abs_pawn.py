#! /usr/bin/env python3
import string
alphabet=string.ascii_uppercase[0:8] #string used for chess board
lb = alphabet.index("B")
ub = alphabet.index("G")

class AbsPawn:
    """Most basic piece of chess """
    def __init__(self,c,a):
        self.piece="Pawn"
        self.color=bool(c)
        self.army=str(a)

    def pawnMoves(self,x,y):
        """Put moves in listP"""
        listP=[]
        if self.color:
            listP+=[(alphabet[alphabet.index(x)],y+1)]
            listP+=[(alphabet[alphabet.index(x)],y+2)]

            if alphabet.index("H")>=alphabet.index(x)+1 and y<8:
                listP+=[(alphabet[alphabet.index(x)+1],y+1)]

            if alphabet.index("A")<=alphabet.index(x)-1 and y<8:
                listP+=[(alphabet[alphabet.index(x)-1],y+1)]
        
        else:
            listP+=[(alphabet[alphabet.index(x)],y-1)]
            listP+=[(alphabet[alphabet.index(x)],y-2)]

            if alphabet.index("H")>=alphabet.index(x)+1 and y>1:
                listP+=[(alphabet[alphabet.index(x)+1],y-1)]

            if alphabet.index("A")<=alphabet.index(x)-1 and y>1:
                listP+=[(alphabet[alphabet.index(x)-1],y-1)]
        """Remove uncorrect moves from listP"""
        listR=[]
        for i in listP:
            if i[1]>8 or i[1]<1:
                listR+=[i]
        for i in listR:
            listP.remove(i)
        
        """Return correct moves"""
        return listP
        
