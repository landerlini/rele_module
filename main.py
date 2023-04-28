"""
Software interface to the 8CH RELE MODULE developed at INFN Firenze.
(c) 2023 - INFN Firenze

Authors: Roberto Ciaranfi, Giovanni Passaleva, Lucio Anderlini
"""

import time

import fastapi

from RelaisUpdater import RelaisUpdater
from fastapi import FastAPI

app = FastAPI()
relais_board = RelaisUpdater()
relais_board.start()


@app.get("/")
async def root():
    return "8CH RELE MODULE Controller (by Ciaranfi with Love)"

@app.get("/set")
async def set_status(q: str):
    try:
        relais_board.status = int(q, base=2)
    except ValueError as e:
        fastapi.HTTPException(str(e))

    return "Ok"


@app.get("/show")
async def run_show(n_iterations: int = 2):
    print ("Show")
    relais_board.status = 0xff
    time.sleep(0.5)
    relais_board.status = 0x0
    time.sleep(0.5)

@app.on_event("shutdown")
def shutdown():
    relais_board.kill()
