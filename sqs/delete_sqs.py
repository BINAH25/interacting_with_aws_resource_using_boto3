import boto3
from botocore.exceptions import ClientError

# Create SQS client
sqs = boto3.client('sqs')

# List all queues
response = sqs.list_queues()

# Get the URL of the first queue (assuming there is at least one)
if 'QueueUrls' in response and len(response['QueueUrls']) > 0:
    sqs_url = response['QueueUrls'][0]
    
    # Delete the queue
    sqs.delete_queue(QueueUrl=sqs_url)
    print(f"Queue {sqs_url} deletion initiated.")
    
    # Check if the queue is still present
    try:
        response = sqs.list_queues()
        if sqs_url not in response.get('QueueUrls', []):
            print("Queue successfully deleted.")
        else:
            print("Queue still exists.")
    except ClientError as e:
        print(f"Error listing queues: {e}")
else:
    print("No queues found.")
