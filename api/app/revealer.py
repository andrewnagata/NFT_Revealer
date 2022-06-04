import os
from s3_adapter import file_exists, reveal_source
from web3_adapter import getMaxSupply
from models import Event

def init():
    #total_minted = getMaxSupply()
    total_minted = 1
    print(f"Revealer initialized at index: {total_minted}")

    # On initialization, go back in history to make sure tokenIDs have been uploaded
    # It could be that this process was down for a while, and the revealer needs to catch up

    # TODO implement this
    last_token = 0
    unrevealed_count = total_minted - last_token

def new_event(event: Event):
    """A new event from the mempool arrived. check out to see if it is a mint confirmation."""

    if event.status != "confirmed":
        return
    if event.contractCall.methodName != "publicMint":
        return

    print("We have a new event uploading files...")

    start_index = getMaxSupply()
    count = int(event.contractCall.params["count"])
    end_index = start_index + count

    for next in range(start_index, end_index):
        # Get files for index
        image_file = str(next) + ".jpg"
        meta_file = str(next)

        reveal_source(image_file)
        print(f"Uploaded image: {image_file}")

        reveal_source("metadata/" + meta_file)
        print(f"Uploaded metadata: {meta_file}")

        print(f"Upload complete for token: {next}")
