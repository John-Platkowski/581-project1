
#This class will only really store the board state & functions
#PLEASE FEEL FREE TO MAKE EDITS JUST INSURE THAT YOU CHANGE OTHER CORRESPONDING CALLS
class Minesweeper:
    def __init__(self, x, y, n):
        self.matrix = self.MineAlgorithm(x, y, n)
        #Board sizes
        self.x_size = 10
        self.y_size = 10
        #Array to track where RecOpen has been
        self.visited = [[0] * self.x_size for _ in range(self.y_size)]

    def RecOpen(self, x, y):
        #Check if the coords passed in are invalid 
        if x < 0 or y < 0 or x >= self.x_size or y >= self.y_size:
            return
        #Check if we have already checked this square
        if self.visited[x][y] > 0:
            return

        #Check for mines in near by squares
        adjacentMines = self.CheckSquare(x,y)
        #Set this tile to be visited
        self.visited[x][y] = 1
        #We only want to reveal tiles if this square has no mines near it
        if adjacentMines == 0:
            #Update the matrix to show that this square is uncovered
            #Note: I just picked 5 because it was the next positive number. We can change if needed
            self.matrix[x][y] = 5

            #Check all adjacent tiles
            self.RecOpen(x,y+1) #Up
            self.RecOpen(x+1,y) #Right
            self.RecOpen(x,y-1) #Down
            self.RecOpen(x-1,y) #Left

            self.RecOpen(x+1,y+1) #Top right diagonal
            self.RecOpen(x-1,y+1) #Top left diagonal
            self.RecOpen(x+1,y-1) #Bottom right diagonal
            self.RecOpen(x-1,y-1) #Bottom left diagonal
        else:
            #Update to indicate there are nearby mines
            self.matrix[x][y] = 2
        return

    def CheckSquare(self, x, y):
        #this should return square state / adjacent bombs
        #this might require more than just this function

        #Note from Tyler: I'm assuming in RecOpen that this will return an integer that represents the number
        #of mines bordering the cell given
        #If you implement it differently, let me know and I will update RecOpen
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
