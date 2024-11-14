import boto3
from botocore.exceptions import ClientError

def delete_bucket(bucket_name):
    s3_client = boto3.client('s3')

    try:
        # List all objects in the bucket and delete them
        objects = s3_client.list_objects_v2(Bucket=bucket_name)
        if 'Contents' in objects:
            for obj in objects['Contents']:
                s3_client.delete_object(Bucket=bucket_name, Key=obj['Key'])
                print(f"Deleted {obj['Key']} from {bucket_name}")

        # Now delete the bucket
        s3_client.delete_bucket(Bucket=bucket_name)
        print(f"Bucket {bucket_name} deleted successfully.")
    
    except ClientError as e:
        print(f"Error: {e}")
        return False
    
    return True

bucket_name = 'louis-new-bucket'  
delete_bucket(bucket_name)
