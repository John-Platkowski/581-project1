# main.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from Minesweeper import Minesweeper
from fastapi.responses import FileResponse

app = FastAPI()
game = None

# pydantic schemas
class clickRequest(BaseModel):
    x: int
    y: int

class setupRequest(BaseModel):
    x: int
    y: int
    n: int
    
# fastapi endpoints to be used

# endpoint to provide the frontend
@app.get("/")
def index():
    return FileResponse("frontend/index.html")

# endpoint to retrieve the board state, this is the only way for the code to get board state
# THIS RETURNS NUMERIC VALUES FOR EVERY SQUARE
# 0 MEAN IT HAS BEEN VISITED AND NIL / NONE MEANS IT HASN"T
# OTHER NUMBERS REPRESENTE ADJACENT BOMB COUNT
@app.get("/board")
def getState():
    if game:
        return { "board": game.visited }
    else:
        raise HTTPException(status_code=404, detail="Board not found")

# endpoint that takes the board configuration values and initializes the game state
## THIS NEEDS TO BE REMOVED OR MOVED TO BASIC CLICK/BOARD ENDPOINT
@app.post("/setup")
def setupGame(setup: setupRequest):
    global game

    game = Minesweeper(setup.x, setup.y, setup.n)


####THESE FUNCTIONS SHOULDN"T RETURN BOARD & OUTCOME/BOARD UPDATE IS BROKEN
# endpoint that provides functionality for updating the board state
@app.post("/board")
def boardUpdate(click: clickRequest):
    if game:
        game.Outcome(click.x, click.y)

        return { "board": game.matrix }
    else:
        raise HTTPException(status_code=404, detail="Board not found")

# endpoint that handles requests requiring flagging functionality
@app.post("/flag")
def flagCell(click: clickRequest):
    if game:
        game.Flag(click.x, click.y)
        return { "board": game.matrix }
    else:
        raise HTTPException(status_code=404, detail="Board not found")
