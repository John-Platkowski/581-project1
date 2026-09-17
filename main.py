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

# endpoint to retrieve the board state if needed
@app.get("/board")
def getState():
    if game:
        return { "board": game.matrix }
    else:
        raise HTTPException(status_code=404, detail="Board not found")

# endpoint that takes the board configuration values and initializes the game state
@app.post("/setup")
def setupGame(setup: setupRequest):
    global game

    game = Minesweeper(setup.x, setup.y, setup.n)
    return { "board": game.matrix }

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
