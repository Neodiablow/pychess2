#! /usr/bin/env python3
import string
from Core.Pieces.abs_pawn import AbsPawn

alphabet=string.ascii_uppercase[0:8] #string used for chess board
lb = alphabet.index("B")
ub = alphabet.index("G")

class NPawn(AbsPawn):
    def moves(self,x,y):
       """Put moves in listP"""
        listP=[]
        if self.color:
            listP+=[(alphabet[alphabet.index(x)],y+1)]
            listP+=[(alphabet[alphabet.index(x)],y+2)]

            if alphabet.index("H")>=alphabet.index(x)+1 and y<8:
                listP+=[(alphabet[alphabet.index(x)+1],y+1)]
                listP+=[(alphabet[alphabet.index(x)+1],y)]

            if alphabet.index("A")<=alphabet.index(x)-1 and y<8:
                listP+=[(alphabet[alphabet.index(x)-1],y+1)]
                listP+=[(alphabet[alphabet.index(x)-1],y)]
        
        else:
            listP+=[(alphabet[alphabet.index(x)],y-1)]
            listP+=[(alphabet[alphabet.index(x)],y-2)]

            if alphabet.index("H")>=alphabet.index(x)+1 and y>1:
                listP+=[(alphabet[alphabet.index(x)+1],y-1)]
                listP+=[(alphabet[alphabet.index(x)+1],y)]

            if alphabet.index("A")<=alphabet.index(x)-1 and y>1:
                listP+=[(alphabet[alphabet.index(x)-1],y-1)]
                listP+=[(alphabet[alphabet.index(x)-1],y)]
        """Remove uncorrect moves from listP"""
        listR=[]
        for i in listP:
            if i[1]>8 or i[1]<1:
                listR+=[i]
        for i in listR:
            listP.remove(i)
        
        """Return correct moves"""
        return listP
        
 
