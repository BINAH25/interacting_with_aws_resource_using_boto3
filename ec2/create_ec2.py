from dotenv import load_dotenv
import boto3
from botocore.exceptions import ClientError

import os
load_dotenv()

# Initialize EC2 resource
ec2 = boto3.resource('ec2')

# Create EC2 instance
try:
    instances = ec2.create_instances(
        ImageId=os.getenv('Image_ID'), 
        MinCount=int(os.getenv('Min_Count')),                    
        MaxCount=int(os.getenv('Max_Count')),                    
        InstanceType=os.getenv('Instance_Type'),        
        KeyName=os.getenv('Key_Name'),         
        TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags': [
                    {'Key': 'Name', 'Value': 'MyEC2Instance'}
                ]
            }
        ]
    )
    print(f'EC2 instance created with ID: {instances[0].id}')

except ClientError as e:
    # Catch specific AWS service exceptions from Boto3
    print(f'An error occurred: {e}')

