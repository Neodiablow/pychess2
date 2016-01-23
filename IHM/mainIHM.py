#! /usr/bin/env python3

from tkinter import * 
from threading import *
import time

plateau = 0
fenetre = 0
canvas = 0

blackKing = 0
whiteKing = 0
blackQueen = 0
whiteQueen = 0
blackBishop = 0
whiteBishop = 0
blackKnight = 0
whiteKnight = 0
blackRook = 0
whiteRook = 0
blackPawn = 0
whitePawn = 0
blackPalmTree = 0
whitePalmTree = 0
blackTiger = 0
whiteTiger = 0
blackElephant = 0
whiteElephant = 0

selected = 0
selectedx = 0
selectedy = 0

listPossibleMoves = []

class MainIHMBoard(Thread):
    def __init__(self, tea1, tea2, callbackM, callbackInfosP):
        global callbackMove
        callbackMove = callbackM
        global callbackInfosPieces
        callbackInfosPieces = callbackInfosP
        global team1
        team1 = tea1
        global team2
        team2 = tea2

        Thread.__init__(self)
        #init()
            
    def Intercepte(self): 
        fenetre.destroy() 
                
    def init(self):
        global fenetre
        fenetre = Tk()
            
        self.createPlateau()
        #self.initPlateau()
          
        fenetre.protocol("WM_DELETE_WINDOW", self.Intercepte) 
            
        fenetre.mainloop()
        
    def run(self):
        self.init()
            
    def click(self,event):
        global selected
        global selectedx
        global selectedy
        x = int(event.x / 50)
        y = int(event.y / 50)
        move = False
        for [x1,y1] in listPossibleMoves:
            if x == x1 and y == y1:
                move = True
        
        if x == selectedx and y == selectedy:
            self.unselect(x, y)
        elif move:
            global callbackMove
            callbackMove(selectedx,selectedy,x,y)
            self.unselect(x, y)
        elif plateau[x][y] != 0:
            self.select(x, y)
        else:
            self.unselect(x, y)
                
                    
    def select(self, x, y):
        self.unselect(x, y)
        global selected
        global selectedx
        global selectedy
        selected = 1
        selectedx = x
        selectedy = y
        callbackInfosPieces(x, y)
        
    def setInfosPiecesIHM(self, x1, y1, listPossibleM):
        global listPossibleMoves
        listPossibleMoves = listPossibleM
        listPossibleMoves.append([x1,y1])
        for [x,y] in listPossibleMoves:
            canvas.create_rectangle(x*50, y*50, (x+1)*50, (y+1)*50, fill="blue", tags="select")
            canvas.tag_raise(plateau[x][y])
        
            
    def unselect(self, x, y):
        global selected
        global selectedx
        global selectedy
        global fenetre
        global canvas
        global listPossibleMoves
        listPossibleMoves = []
        selected = 0
        selectedx = 0
        selectedy = 0
        canvas.delete(fenetre, "select")
                
            
    def createPlateau(self):
        global fenetre
        global plateau
        global canvas
        plateau = [[0 for i in range(8)] for i in range(8)]
        canvas = Canvas(fenetre, width=400, height=400, background='yellow')
            
        for d1 in range(8):
            for d2 in range(8):
                if (d1+d2)%2 == 0:
                    ligne1 = canvas.create_rectangle(d1*50, d2*50, (d1+1)*50, (d2+1)*50, fill="white")
                else:
                    ligne2 = canvas.create_rectangle(d1*50, d2*50, (d1+1)*50, (d2+1)*50, fill="black")
                        
                        
        canvas.pack()
            
        canvas.bind('<Button-1>', self.click)
        
        global blackKing
        global whiteKing
        global blackQueen
        global whiteQueen
        global blackBishop
        global whiteBishop
        global blackKnight
        global whiteKnight
        global blackRook
        global whiteRook
        global blackPawn
        global whitePawn
        global blackPalmTree
        global whitePalmTree
        global blackTiger
        global whiteTiger
        global blackElephant
        global whiteElephant
        
        blackKing = PhotoImage(file="IHM/pictures/blackKing.png")
        whiteKing = PhotoImage(file="IHM/pictures/whiteKing.png")
        blackQueen = PhotoImage(file="IHM/pictures/blackQueen.png")
        whiteQueen = PhotoImage(file="IHM/pictures/whiteQueen.png")
        blackBishop = PhotoImage(file="IHM/pictures/blackBishop.png")
        whiteBishop = PhotoImage(file="IHM/pictures/whiteBishop.png")
        blackKnight = PhotoImage(file="IHM/pictures/blackKnight.png")
        whiteKnight = PhotoImage(file="IHM/pictures/whiteKnight.png")
        blackRook = PhotoImage(file="IHM/pictures/blackRook.png")
        whiteRook = PhotoImage(file="IHM/pictures/whiteRook.png")
        blackPawn = PhotoImage(file="IHM/pictures/blackPawn.png")
        whitePawn = PhotoImage(file="IHM/pictures/whitePawn.png")
        blackPalmTree = PhotoImage(file="IHM/pictures/blackPalmTree.png")
        whitePalmTree = PhotoImage(file="IHM/pictures/whitePalmTree.png")
        blackTiger = PhotoImage(file="IHM/pictures/blackTiger.png")
        whiteTiger = PhotoImage(file="IHM/pictures/whiteTiger.png")
        blackElephant = PhotoImage(file="IHM/pictures/blackElephant.png")
        whiteElephant = PhotoImage(file="IHM/pictures/whiteElephant.png")
        
        blackKing = blackKing.subsample(2, 2)
        whiteKing = whiteKing.subsample(2, 2)
        blackQueen = blackQueen.subsample(2, 2)
        whiteQueen = whiteQueen.subsample(2, 2)
        blackBishop = blackBishop.subsample(2, 2)
        whiteBishop = whiteBishop.subsample(2, 2)
        blackKnight = blackKnight.subsample(2, 2)
        whiteKnight = whiteKnight.subsample(2, 2)
        blackRook = blackRook.subsample(2, 2)
        whiteRook = whiteRook.subsample(2, 2)
        blackPawn = blackPawn.subsample(2, 2)
        whitePawn = whitePawn.subsample(2, 2)
        blackPalmTree = blackPalmTree.subsample(2, 2)
        whitePalmTree = whitePalmTree.subsample(2, 2)
        blackTiger = blackTiger.subsample(2, 2)
        whiteTiger = whiteTiger.subsample(2, 2)
        blackElephant = blackElephant.subsample(2, 2)
        whiteElephant = whiteElephant.subsample(2, 2)
        
    def addPiece(self, x, y, type):
        global plateau
        global canvas
        
        if type=="blackKing":
            plateau[x][y] = canvas.create_image(x*50+25, y*50+25, image=blackKing)
        elif type=="whiteKing":
            plateau[x][y] = canvas.create_image(x*50+25, y*50+25, image=whiteKing)
        elif type=="blackQueen":
            plateau[x][y] = canvas.create_image(x*50+25, y*50+25, image=blackQueen)
        elif type=="whiteQueen":
            plateau[x][y] = canvas.create_image(x*50+25, y*50+25, image=whiteQueen)
        elif type=="blackBishop":
            plateau[x][y] = canvas.create_image(x*50+25, y*50+25, image=blackBishop)
        elif type=="whiteBishop":
            plateau[x][y] = canvas.create_image(x*50+25, y*50+25, image=whiteBishop)
        elif type=="blackKnight":
            plateau[x][y] = canvas.create_image(x*50+25, y*50+25, image=blackKnight)
        elif type=="whiteKnight":
            plateau[x][y] = canvas.create_image(x*50+25, y*50+25, image=whiteKnight)
        elif type=="whiteRook":
            plateau[x][y] = canvas.create_image(x*50+25, y*50+25, image=whiteRook)
        elif type=="blackRook":
            plateau[x][y] = canvas.create_image(x*50+25, y*50+25, image=blackRook)
        elif type=="blackPawn":
            plateau[x][y] = canvas.create_image(x*50+25, y*50+25, image=blackPawn)
        elif type=="whitePawn":
            plateau[x][y] = canvas.create_image(x*50+25, y*50+25, image=whitePawn)
        elif type=="blackJungleQueen":
            plateau[x][y] = canvas.create_image(x*50+25, y*50+25, image=blackPalmTree)
        elif type=="whiteJungleQueen":
            plateau[x][y] = canvas.create_image(x*50+25, y*50+25, image=whitePalmTree)
        elif type=="whiteTiger":
            plateau[x][y] = canvas.create_image(x*50+25, y*50+25, image=whiteTiger)
        elif type=="blackTiger":
            plateau[x][y] = canvas.create_image(x*50+25, y*50+25, image=blackTiger)
        elif type=="blackElephant":
            plateau[x][y] = canvas.create_image(x*50+25, y*50+25, image=blackElephant)
        elif type=="whiteElephant":
            plateau[x][y] = canvas.create_image(x*50+25, y*50+25, image=whiteElephant)
            
    def moveIHM(self, x1, y1, x2, y2):
        global plateau
        global canvas
        
        item=plateau[x1][y1]
        
        xpos = x1*50 + 25
        ypos = y1*50 + 25
        
        xfin = x2*50 + 25
        yfin = y2*50 + 25
        
        deltax = (xfin - xpos) / 50
        deltay = (yfin - ypos) / 50
        
        
        for i in range(0,50):
            canvas.move(plateau[x1][y1], deltax, deltay)
            canvas.update()
            item=plateau[x1][y1]
            time.sleep(0.01)
        
        canvas.move(plateau[x1][y1], xfin - canvas.coords(item)[0], yfin - canvas.coords(item)[1])
        canvas.update()
        
        if plateau[x2][y2] != 0:
            self.delPieceIHM(x2, y2)
        
        plateau[x2][y2] = plateau[x1][y1]
        plateau[x1][y1] = 0
        
    def delPieceIHM(self, x, y):
        global canvas
        canvas.delete(plateau[x][y])
        plateau[x][y] = 0
        
