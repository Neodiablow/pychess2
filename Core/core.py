from threading import *
from Core.Pieces.rook import Rook
from Core.Pieces.knight import Knight
from Core.Pieces.bishop import Bishop
from Core.Pieces.king import King
from Core.Pieces.queen import Queen
from Core.Pieces.junglequeen import JungleQueen
from Core.Pieces.tiger import Tiger
from Core.Pieces.elephant import Elephant
from Core.Pieces.pawn import Pawn
import string

plateau = 0
team1 = 0
team2 = 0

alphabet = string.ascii_uppercase[0:8]


class Core(Thread):
    def __init__(self, tea1, tea2):
        global team1
        global team2
        team1 = tea1
        team2 = tea2
    
        Thread.__init__(self)
        
    def run(self):
        print ("Core Run")
        self.createPlateau()
        
    def getIndex(self, letter):
        return alphabet.index(letter)
        
    def getLetter(self, index):
        return alphabet[index]
        
    def createPlateau(self):
        global plateau
        plateau = [[0 for i in range(8)] for i in range(8)]
        
    def initPlateau(self, threadIHM):
        if team1 == "Classical":
            self.addPiece(0,0, "Rook", False, team1, threadIHM)
            self.addPiece(1,0, "Knight", False, team1, threadIHM)
            self.addPiece(2,0, "Bishop", False, team1, threadIHM)
            self.addPiece(3,0, "King", False, team1, threadIHM)
            self.addPiece(4,0, "Queen", False, team1, threadIHM)
            self.addPiece(5,0, "Bishop", False, team1, threadIHM)
            self.addPiece(6,0, "Knight", False, team1, threadIHM)
            self.addPiece(7,0, "Rook", False, team1, threadIHM)
            self.addPiece(0,1, "Pawn", False, team1, threadIHM)
            self.addPiece(1,1, "Pawn", False, team1, threadIHM)
            self.addPiece(2,1, "Pawn", False, team1, threadIHM)
            self.addPiece(3,1, "Pawn", False, team1, threadIHM)
            self.addPiece(4,1, "Pawn", False, team1, threadIHM)
            self.addPiece(5,1, "Pawn", False, team1, threadIHM)
            self.addPiece(6,1, "Pawn", False, team1, threadIHM)
            self.addPiece(7,1, "Pawn", False, team1, threadIHM)
        elif team1 == "Animals":
            self.addPiece(0,0, "Elephant", False, team1, threadIHM)
            self.addPiece(1,0, "Knight", False, team1, threadIHM)
            self.addPiece(2,0, "Tiger", False, team1, threadIHM)
            self.addPiece(3,0, "King", False, team1, threadIHM)
            self.addPiece(4,0, "JungleQueen", False, team1, threadIHM)
            self.addPiece(5,0, "Tiger", False, team1, threadIHM)
            self.addPiece(6,0, "Knight", False, team1, threadIHM)
            self.addPiece(7,0, "Elephant", False, team1, threadIHM)
            self.addPiece(0,1, "Pawn", False, team1, threadIHM)
            self.addPiece(1,1, "Pawn", False, team1, threadIHM)
            self.addPiece(2,1, "Pawn", False, team1, threadIHM)
            self.addPiece(3,1, "Pawn", False, team1, threadIHM)
            self.addPiece(4,1, "Pawn", False, team1, threadIHM)
            self.addPiece(5,1, "Pawn", False, team1, threadIHM)
            self.addPiece(6,1, "Pawn", False, team1, threadIHM)
            self.addPiece(7,1, "Pawn", False, team1, threadIHM)
        
        if team2 == "Classical":
            self.addPiece(0,7, "Rook", True, team2, threadIHM)
            self.addPiece(1,7, "Knight", True, team2, threadIHM)
            self.addPiece(2,7, "Bishop", True, team2, threadIHM)
            self.addPiece(3,7, "King", True, team2, threadIHM)
            self.addPiece(4,7, "Queen", True, team2, threadIHM)
            self.addPiece(5,7, "Bishop", True, team2, threadIHM)
            self.addPiece(6,7, "Knight", True, team2, threadIHM)
            self.addPiece(7,7, "Rook", True, team2, threadIHM)
            self.addPiece(0,6, "Pawn", True, team2, threadIHM)
            self.addPiece(1,6, "Pawn", True, team2, threadIHM)
            self.addPiece(2,6, "Pawn", True, team2, threadIHM)
            self.addPiece(3,6, "Pawn", True, team2, threadIHM)
            self.addPiece(4,6, "Pawn", True, team2, threadIHM)
            self.addPiece(5,6, "Pawn", True, team2, threadIHM)
            self.addPiece(6,6, "Pawn", True, team2, threadIHM)
            self.addPiece(7,6, "Pawn", True, team2, threadIHM)
        elif team2 == "Animals":
            self.addPiece(0,7, "Elephant", True, team2, threadIHM)
            self.addPiece(1,7, "Knight", True, team2, threadIHM)
            self.addPiece(2,7, "Tiger", True, team2, threadIHM)
            self.addPiece(3,7, "King", True, team2, threadIHM)
            self.addPiece(4,7, "JungleQueen", True, team2, threadIHM)
            self.addPiece(5,7, "Tiger", True, team2, threadIHM)
            self.addPiece(6,7, "Knight", True, team2, threadIHM)
            self.addPiece(7,7, "Elephant", True, team2, threadIHM)
            self.addPiece(0,6, "Pawn", True, team2, threadIHM)
            self.addPiece(1,6, "Pawn", True, team2, threadIHM)
            self.addPiece(2,6, "Pawn", True, team2, threadIHM)
            self.addPiece(3,6, "Pawn", True, team2, threadIHM)
            self.addPiece(4,6, "Pawn", True, team2, threadIHM)
            self.addPiece(5,6, "Pawn", True, team2, threadIHM)
            self.addPiece(6,6, "Pawn", True, team2, threadIHM)
            self.addPiece(7,6, "Pawn", True, team2, threadIHM)
    
    def addPiece(self, x, y, type, colorBool, team, threadIHM):
        global plateau
        if colorBool:
            color = "white"
        else:
            color = "black"
            
        if type == "Rook":
            plateau[x][y] = Rook(colorBool,team);
        elif type == "Knight":
            plateau[x][y] = Knight(colorBool,team);
        elif type == "Bishop":
            plateau[x][y] = Bishop(colorBool,team);
        elif type == "King":
            plateau[x][y] = King(colorBool,team);
        elif type == "Queen":
            plateau[x][y] = Queen(colorBool,team);
        elif type == "JungleQueen":
            plateau[x][y] = JungleQueen(colorBool,team);
        elif type == "Tiger":
            plateau[x][y] = Tiger(colorBool,team);
        elif type == "Elephant":
            plateau[x][y] = Elephant(colorBool,team);
        else:
            plateau[x][y] = Pawn(colorBool,team);
            
        threadIHM.addPiece(x,y, color + type)
        
    def getPossibleMoves(self, x1, y1):
        listPossibleMovesL = plateau[x1][y1].moves(self.getLetter(x1),8-y1)
        listPossibleMoves = []
        for (x,y) in listPossibleMovesL:
            listPossibleMoves.append([self.getIndex(x),8-y])
        return listPossibleMoves
        
    def isMoveOk(self, x1, y1, x2, y2):
        xL1 = self.getLetter(x1)
        yL1 = 8-y1
        xL2 = self.getLetter(x2)
        yL2 = 8-y2
        
        plateau[x2][y2] = plateau[x1][y1]
        plateau[x1][y1] = 0
      
        return True