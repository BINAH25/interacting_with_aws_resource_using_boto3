import boto3
from botocore.exceptions import ClientError
import os

def download_file_from_s3(bucket, object_name, file_name=None):
    # If a local file name is not specified, use the object_name
    if file_name is None:
        file_name = object_name

    # Initialize an S3 client
    s3_client = boto3.client('s3')

    try:
        # Download the file from S3
        s3_client.download_file(bucket, object_name, file_name)
        print(f"File {object_name} downloaded successfully to {file_name}")
    except ClientError as e:
        print(f"Error occurred: {e}")
        return False
    return True

bucket_name = 'louis-new-bucket' 
object_name = 'cat.jpg'           
local_file_name = 'downloaded_cat.jpg' 

# Call the function
download_file_from_s3(bucket_name, object_name, local_file_name)
