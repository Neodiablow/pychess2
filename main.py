#! /usr/bin/env python3
from IHM.mainIHM import MainIHMBoard
from Core.core import Core
import time

threadIHM = 0
threadCore = 0

def callbackMove(x1, y1, x2, y2):
    global mainIHMBoard
    if threadCore.isMoveOk(x1, y1, x2, y2):
        threadIHM.moveIHM(x1, y1, x2, y2)
    else:
        threadIHM.unselect(x1, y1)
    
def callbackInfosPieces(x1, y1):
    listPossibleMoves = []
    #== Pour tester ==
    listPossibleMoves.append([x1+1,y1])
    listPossibleMoves.append([x1,y1+1])
    listPossibleMoves.append([x1-1,y1])
    listPossibleMoves.append([x1,y1-1])
    #== Fin pour tester
    listPossibleMoves = threadCore.getPossibleMoves(x1, y1)
    threadIHM.setInfosPiecesIHM(x1, y1, listPossibleMoves)
    
#Création du core du jeu
threadCore = Core("Classical", "Animals")
threadCore.start()
#Création de l'IHM
threadIHM = MainIHMBoard("Classical", "Animals", callbackMove, callbackInfosPieces)
threadIHM.start()

#ça sera à améliorer ça
time.sleep(1)
threadCore.initPlateau(threadIHM)


#Boucle pour tester le thread
#while True:
#    input("Console: ")
