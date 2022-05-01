import boto3
import os
from dotenv import load_dotenv

load_dotenv()

KEY = os.getenv('AWS_ACCESS_KEY')
SECRET = os.getenv('AWS_SECRET_KEY')

s3 = boto3.client('s3',
         aws_access_key_id=KEY,
         aws_secret_access_key=SECRET)

# Upload a new file
s3.upload_file(
    'east.JPG',
    'pizzapalsmedia',
    Key='meta/east.JPG',
    ExtraArgs={ "ContentType": "image/jpeg"}
)

print("Uploaded a file!!")
