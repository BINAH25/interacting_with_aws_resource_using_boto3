import logging
import boto3
from botocore.exceptions import ClientError
import os


def upload_file(file_name, bucket, object_name=None):
    
    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    s3_client = boto3.client('s3')
    # Upload the file
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
        print("print file uploaded successfully")
    except ClientError as e:
        logging.error(e)
        return False
    return True


file = os.path.join(os.path.dirname(__file__), 'cat.jpg')
bucket = 'louis-new-bucket'

upload_file(file,bucket)