#! /usr/bin/env python3

from IHM.mainIHM import MainIHMBoard,moveIHM,setInfosPiecesIHM


def callbackMove(x1, y1, x2, y2):
    global mainIHMBoard
    moveIHM(x1, y1, x2, y2)
    
def callbackInfosPieces(x1, y1):
    listPossibleMoves = []
    #== Pour tester ==
    listPossibleMoves.append([x1+1,y1])
    listPossibleMoves.append([x1,y1+1])
    listPossibleMoves.append([x1-1,y1])
    listPossibleMoves.append([x1,y1-1])
    #== Fin pour tester
    setInfosPiecesIHM(x1, y1, listPossibleMoves)
    
mainIHMBoard = MainIHMBoard("normal", "animaux", callbackMove, callbackInfosPieces)

while True:
    input("Console: ")
