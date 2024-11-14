import logging
import boto3
from botocore.exceptions import ClientError

def create_bucket(bucket_name, region=None):
    # Create bucket
    try:
        if region is None:
            # Use the default region (us-east-1)
            s3_client = boto3.client('s3')
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            # Create the bucket in a region other than us-east-1
            s3_client = boto3.client('s3', region_name=region)
            if region == 'us-east-1':
                s3_client.create_bucket(Bucket=bucket_name)
            else:
                # Set location constraint for other regions
                location = {'LocationConstraint': region}
                s3_client.create_bucket(Bucket=bucket_name,
                                        CreateBucketConfiguration=location)

        response = s3_client.head_bucket(Bucket=bucket_name)
        print(f"Bucket '{bucket_name}' created successfully!")
        print(f"Bucket details: {response}")

        print(f"Region: {region if region else 'us-east-1'}")
        return True

    except ClientError as e:
        logging.error(e)
        return False


bucket_name = input("Enter bucket name\n")
region = input("enter your prefer region\n")

if region:
    create_bucket(bucket_name, region)

else:
    create_bucket(bucket_name)