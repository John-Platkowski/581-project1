
#This class will only really store the board state & functions
#PLEASE FEEL FREE TO MAKE EDITS JUST INSURE THAT YOU CHANGE OTHER CORRESPONDING CALLS
class Minesweeper:
    def __init__(self, x, y, n):
        self.matrix = self.MineAlgorithm(x, y, n)

    def RecOpen(self, x, y):
        #this should recursively open squares (no adjacent bombs)
        pass

    def CheckSquare(self, x, y):
        #this should return square state / adjacent bombs
        #this might require more than just this function
        pass

    def MineAlgorithm(self, x, y, n):
        pass

    #Nothing should return matrix, should just use internal
    #UI should only call outcome and flag, use self.matrix
    def Outcome(self, x, y):
        #this should determine game outcome/win/loss
        pass

    def Flag(self, x, y):
        #this should flag a square
        #ensure that other information is not lost
        pass
