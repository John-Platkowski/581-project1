# main.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from Minesweeper import Minesweeper
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

game = None
mine_count = 10

# pydantic schemas
class clickRequest(BaseModel):
    x: int
    y: int

class setupRequest(BaseModel):
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
    global mine_count
    global game

    mine_count = setup.n
    game = None

####THESE FUNCTIONS SHOULDN"T RETURN BOARD & OUTCOME/BOARD UPDATE IS BROKEN
# endpoint that provides functionality for updating the board state
@app.post("/board")
def boardUpdate(click: clickRequest):
    global game

    if game is None:
        game = Minesweeper(click.x,click.y,mine_count)
    
    result = game.Outcome(click.x, click.y)

    return {
            "board": game.visited,
            "result": result,
            "mines": game.RemainingMines()
            }


# endpoint that handles requests requiring flagging functionality
@app.post("/flag")
def flagCell(click: clickRequest):
    if game:
        game.Flag(click.x, click.y)
        return { 
            "board": game.visited,
            "mines": game.RemainingMines()
            }
    else:
        raise HTTPException(status_code=404, detail="Board not found")
