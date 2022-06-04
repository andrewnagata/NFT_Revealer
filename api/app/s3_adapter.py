import boto3
import botocore
import os
from dotenv import load_dotenv

load_dotenv(verbose=True)

S3_PUBLIC_BUCKET = str(os.getenv('S3_PUBLIC_BUCKET'))
S3_PRIVATE_BUCKET = str(os.getenv('S3_PRIVATE_BUCKET'))
KEY = os.getenv('AWS_ACCESS_KEY')
SECRET = os.getenv('AWS_SECRET_KEY')

s3_resource = boto3.resource('s3',
        aws_access_key_id=KEY,
        aws_secret_access_key=SECRET)

def reveal_source(path: str):
    copy_source = {
        'Bucket': S3_PRIVATE_BUCKET,
        'Key': str(path)
    }

    s3_resource.meta.client.copy(copy_source, S3_PUBLIC_BUCKET, path)

def file_exists(filename: str = None):

    try:
        s3_resource.Object(S3_PRIVATE_BUCKET, filename).load()
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            # The object does not exist.
            return False
    else:
        return True
