"""
Software interface to the 8CH RELE MODULE developed at INFN Firenze.
(c) 2023 - INFN Firenze

Authors: Roberto Ciaranfi, Giovanni Passaleva, Lucio Anderlini
"""

import time
from RelaisUpdater import RelaisUpdater
from fastapi import FastAPI

app = FastAPI()
relais_board = RelaisUpdater()
try:
    relais_board.start()
finally:
    relais_board.kill()


@app.get("/")
async def root():
    return "8CH RELE MODULE Controller (by Ciaranfi with Love)"

@app.get("/set")
async def set(q: int):
    relais_board.status = chr(i)
    return "Ok"


@app.get("/show")
async def run_show(n_iterations: int = 2):
    for loop in range(n_iterations):
        for i in list(range(8)) + list(range(8))[::-1]:
            relais_board.status = 0
            relais_board[i] = True
            time.sleep(0.15)

    relais_board.status = 0

