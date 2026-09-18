
import random
from collections import deque

#Values for self.matrix, but perhaps we want it more coherent/extensible so these are consts
EMPTY = 0
MINE = 1

#This class will only really store the board state & functions
#PLEASE FEEL FREE TO MAKE EDITS JUST INSURE THAT YOU CHANGE OTHER CORRESPONDING CALLS

#VISITED MATRIX CONSTANTS
FLAG = -1
UNVISITED = None
#VISITED = >= 0

class Minesweeper:
    #How many placements MineAlgorithm tries before settling for the last one
    MAX_PLACEMENT_ATTEMPTS = 100

    def __init__(self, x, y, n):
        #Board sizes
        self.x_size = 10
        self.y_size = 10
        #THIS IS THE AUTHORITATIVE LOCATION OF ALL THE BOMBS
        #THIS SHOULD BE TREATED AS STATIC UNLESS STARTING
        self.matrix = self._empty()
        self.visited = self._empty()
        self.MineAlgorithm(x, y, n)

    def RecOpen(self, x, y):
        #Check if the coords passed in are invalid 
        if x < 0 or y < 0 or x >= self.x_size or y >= self.y_size:
            return
        #Check if we have already checked this square
        if self.visited[x][y] is not UNVISITED:
            return

        #Check for mines in near by squares
        adjacentMines = self.CheckSquare(x,y)
        #Uncover this tile. Storing the count is what /board serves, and it doubles as
        #the marker that keeps this recursion from running back over itself
        self.visited[x][y] = adjacentMines
        #We only want to reveal tiles if this square has no mines near it
        if adjacentMines == 0:
            #Check all adjacent tiles
            for neighbor in self._Neighbors(x, y):
                 self.RecOpen(*neighbor)
        return

    def CheckSquare(self, x, y):
        #Returns how many mines border (x, y)
        count = 0
        for nx, ny in self._Neighbors(x, y):
            if self.matrix[nx][ny] == MINE:
                count += 1
        return count

    def MineAlgorithm(self, x: int, y: int, n: int) -> list[list[int]]:
        #Spawns n mines in a board such that the first click at (x, y) neither instantly loses nor wins
        #(x, y) and its 8 neighbors start without mines, so (x, y) opens a 0 square
        total = self.x_size * self.y_size
        if not (0 <= n < total):
            raise ValueError(f"cannot place {n} mines on {total} cells")

        #Block x,y and its neighbors
        blocked = {(x, y)}
        for nx, ny in self._Neighbors(x, y):
            blocked.add((nx, ny))
        # Or just block x,y if there are too many bombs to guarantee the neighbors
        if n > total - len(blocked):
            blocked = {(x, y)}

        candidates = []
        for cx in range(self.x_size):
            for cy in range(self.y_size):
                if (cx, cy) not in blocked:
                    candidates.append((cx, cy))

        grid = None
        for _ in range(self.MAX_PLACEMENT_ATTEMPTS):
            grid = [[EMPTY] * self.y_size for _ in range(self.x_size)]
            for cx, cy in random.sample(candidates, n):
                grid[cx][cy] = MINE
            #CheckSquare reads self.matrix, so we have to install candidates now
            self.matrix = grid
            self.visited = self._empty()
            if self.Outcome(x, y) == 2:
                return grid

        return grid

    def _Neighbors(self, x, y):
        #The in bounds cells touching (x, y)
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.x_size and 0 <= ny < self.y_size:
                    yield (nx, ny)

    # def _IsInstantWin(self, x, y, n):
    #     #True when opening (x, y) on self.matrix would uncover every safe cell at once
    #     #Basically RecOpen but BFS to not break recursion depth
    #     seen = {(x, y)}
    #     queue = deque([(x, y)])
    #     while queue:
    #         cx, cy = queue.popleft()
    #         if self.CheckSquare(cx, cy) != 0:
    #             continue
    #         for nx, ny in self._Neighbors(cx, cy):
    #             if (nx, ny) not in seen:
    #                 seen.add((nx, ny))
    #                 queue.append((nx, ny))
    #     return len(seen) == self.x_size * self.y_size - n

    #Nothing should return matrix, should just use internal
    #UI should only call outcome and flag, use self.matrix
    def Outcome(self, x, y):
        if self.matrix[x][y] == MINE:
            return 0
        
        self.RecOpen(x,y)
        total = sum(self.visited[i].count(UNVISITED) for i in range(len(self.visited)))
        total += sum(self.visited[i].count(FLAG) for i in range(len(self.visited)))
        if total == sum(self.matrix[i].count(MINE) for i in range(len(self.matrix))):
            return 1
        
        return 2

        #Can return number of placed flags to make displaying easier
    def Flag(self, x, y):
        #Places a flag on the square if it's uncovered (flag identifier is -1 since other positive numbers represent number of mines)
        if (self.visited[x][y] is UNVISITED):
            self.visited[x][y] = FLAG
        #Remove flag if the square has a flag
        elif (self.visited[x][y] == FLAG):
            self.visited[x][y] = UNVISITED
        #If the flag action is accidentally done on an already uncovered square, do nothing
        else:
            pass
            
        #return sum(self.visited[i].count(-1) for i in range(len(self.visited)))


    def _empty(self):
        return [[UNVISITED] * self.y_size for _ in range(self.x_size)]
