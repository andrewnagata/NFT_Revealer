import boto3
import os
from dotenv import load_dotenv

load_dotenv(verbose=True)
S3_BUCKET_NAME = os.getenv('S3_BUCKET_NAME')
KEY = os.getenv('AWS_ACCESS_KEY')
SECRET = os.getenv('AWS_SECRET_KEY')

s3 = boto3.client('s3',
        aws_access_key_id=KEY,
        aws_secret_access_key=SECRET)

def upload_image(path_to_file: str, filename: str, folder: str = None):

    key = filename  
    if folder != None:
        key = folder + "/" + filename

    s3.upload_file(
        path_to_file,
        S3_BUCKET_NAME,
        Key=key,
        ExtraArgs={ "ContentType": "image/jpeg" }
    )

def upload_metadata(path_to_file: str, filename: str, folder: str = None):
    key = folder + "/" + filename

    s3.upload_file(
        path_to_file,
        S3_BUCKET_NAME,
        Key=key,
        ExtraArgs={ "ContentType": "json" }
    )