
#Values for self.matrix, but perhaps we want it more coherent/extensible so these are consts
EMPTY = 0
MINE = 1

#This class will only really store the board state & functions
#PLEASE FEEL FREE TO MAKE EDITS JUST INSURE THAT YOU CHANGE OTHER CORRESPONDING CALLS
class Minesweeper:
    def __init__(self, x, y, n):

        #THIS IS THE AUTHORITATIVE LOCATION OF ALL THE BOMBS
        #THIS SHOULD BE TREATED AS STATIC UNLESS STARTING
        self.matrix = self.MineAlgorithm(x, y, n)
        #Board sizes
        self.x_size = 10
        self.y_size = 10
        
        #THIS WILL BE THE VISIBLE PART OF THE ARRAY HANDED UP TO THE USER
        #THIS SHOULD BE THE ONLY THING THAT IS EDITED THROUGHOUT THE PROGRAM
        self.visited = [None * self.y_size for _ in range(self.x_size)]

    def RecOpen(self, x, y):
        #Check if the coords passed in are invalid 
        if x < 0 or y < 0 or x >= self.x_size or y >= self.y_size:
            return
        #Check if we have already checked this square
        if self.visited[x][y] is not None:
            return

        #Check for mines in near by squares
        adjacentMines = self.CheckSquare(x,y)
        #Set this tile to be visited
        self.visited[x][y] = adjacentMines
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
        return

    def CheckSquare(self, x, y):
        #Returns how many mines border (x, y)
        count = 0
        for nx, ny in self._Neighbors(x, y):
            if self.matrix[nx][ny] == MINE:
                count += 1
        return count

    def MineAlgorithm(self, x, y, n):
        pass

    #Nothing should return matrix, should just use internal
    #UI should only call outcome and flag, use self.matrix
    def Outcome(self, x, y):
        #this should determine game outcome/win/loss
        #SHOULD RETURN NUMERICAL VALUE TO MATCH
        pass

    def Flag(self, x, y):
        #this should flag a square
        #ensure that other information is not lost
        pass
