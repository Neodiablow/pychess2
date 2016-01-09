#! /usr/bin/env python3
import string
alphabet=string.ascii_uppercase[0:8] #string used for chess board
lb = alphabet.index("B")
ub = alphabet.index("G")

class King:
    """Most important piece of chess"""
    def __init__(self,c,a):
        self.piece="King"
        self.color=bool(c)
        self.army=str(a)
    
    def moves(self,x,y):
        """Returns Valid moves to the model"""
        listK=[]
        if y<8:                                             #if y<8
            listK+=[(x,y+1)]                                #can move upword
        if alphabet.index("H")>alphabet.index(x):           #if x<H
            listK+=[(alphabet[alphabet.index(x)+1],y)]      #can move on the right
        if y>1:                                             #if y>1
            listK+=[(x,y-1)]                                #can move downward
        if alphabet.index("A")<alphabet.index(x):           #if x> A
            listK+=[(alphabet[alphabet.index(x)-1],y)]      #can move on the left
        if y<8 and alphabet.index("H")>alphabet.index(x):   #if y<8 && x<y 
            listK+=[(alphabet[alphabet.index(x)+1],y+1)]    #can move up right
        if y<8 and alphabet.index("A")<alphabet.index(x):   #etc
            listK+=[(alphabet[alphabet.index(x)-1],y+1)]    #up left
        if y>1 and alphabet.index("H")>alphabet.index(x):   #etc
            listK+=[(alphabet[alphabet.index(x)+1],y-1)]    #down right
        if y>1 and alphabet.index("A")<alphabet.index(x):   #etc
            listK+=[(alphabet[alphabet.index(x)-1],y-1)]    #down left
            
        return listK
    
    def smallCastle(self):
        if self.color and self.army == "Classic":
            return ["G",1]
        elif self.army == "Classic":
            return ["G",8]
        else :
            return []
    def bigCastle(self):
        if self.color and self.army == "Classic":
            return ["B",1]
        elif self.army == "Classic":
            return ["B",8]
        else :
            return []
