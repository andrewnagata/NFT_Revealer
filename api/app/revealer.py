import os
from web3_adapter import getMaxSupply
from models import Event

total_minted: int
index: int

def init():
    total_minted = getMaxSupply()
    global index
    index = total_minted - 1 # assume there is token_id 0
    print(f"Revealer initialized at index: {index}")

def new_event(event: Event):
    print("We have a new event")
    if event.status != "confirmed":
        return
    if event.contractCall.methodName != "publicMint":
        return

    global index
    index += 1

    path = "/usr/share/nginx/html/"
    if os.path.exists(path):
        filename = str(index) + ".txt"
        full = os.path.join(path, filename)
        with open(full, 'w') as f:
            f.write('Create a new text file!')
    
            print(f"Uploading files for token_id: {index}")
    else:
        print("no path to write to")
