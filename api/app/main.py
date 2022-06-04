from typing import Optional

from fastapi import FastAPI
#from fastapi.middleware.cors import CORSMiddleware

from models import Event
from revealer import init, new_event

app = FastAPI()

init()

# UNCOMMENT FOR LOCAL TESTING
# origins = [
#     "http://localhost",
#     "http://localhost/event",
# ]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

@app.get("/")
def read_root():
    return {"Hello": "Rolling Revelaer is ready"}


@app.post("/event/")
async def create_item(event: Event):
    new_event(event)
    return {"Event": "something happened"}