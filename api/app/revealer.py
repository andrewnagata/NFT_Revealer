import os
from web3_adapter import getMaxSupply
from models import Event
from s3_adapter import upload_image, upload_metadata

total_minted: int
index: int

def init():
    total_minted = getMaxSupply()
    global index
    index = total_minted - 1 # assume there is token_id 0
    print(f"Revealer initialized at index: {index}")

def new_event(event: Event):
    print("We have a new event uploading files...")
    if event.status != "confirmed":
        return
    if event.contractCall.methodName != "publicMint":
        return

    global index
    index += 1

    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    root_image_path = ROOT_DIR + "../../images"
    root_meta_path = ROOT_DIR + "../../metadata"

    # Get files for index
    image_file = str(index) + ".jpg"
    path_to_image = os.path.join(root_image_path, image_file)
    meta_file = str(index)
    path_to_meta = os.path.join(root_meta_path, meta_file)

    upload_image(path_to_image, image_file)
    print(f"Uploaded image: {image_file}")

    upload_metadata(path_to_meta, meta_file, "meta")
    print(f"Uploaded metadata: {meta_file}")

    print(f"Upload complete for token: {index}")
