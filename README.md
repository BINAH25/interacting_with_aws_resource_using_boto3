# Interacting with AWS Resources Using Boto3

This repository demonstrates how to interact with various AWS services (EC2, S3, and SQS) using **Boto3**, the AWS SDK for Python. It provides a series of scripts for performing common AWS operations such as creating, retrieving, and deleting EC2 instances, S3 buckets, and SQS queues.

## Key Features:

### EC2 Interactions:
- **Create EC2 Instances**: Customize parameters like Image ID, instance type, and key name.
- **Retrieve EC2 Instance Details**: Fetch details of existing EC2 instances.
- **Terminate EC2 Instances**: Delete EC2 instances as needed.

### S3 Interactions:
- **Create and Manage S3 Buckets**: Create, list, and delete S3 buckets.
- **Upload and Download Files to/from S3 Buckets**: Upload and retrieve files from an S3 bucket.
- **Delete S3 Buckets**: Clean up unwanted S3 buckets.

### SQS Interactions:
- **Create, Retrieve, and Delete SQS Queues**: Manage SQS queues with basic operations.

## Setup Instructions:

1. **Clone the Repository:**
   ```bash
    git clone https://github.com/BINAH25/interacting_with_aws_resource_using_boto3.git
    cd interacting_with_aws_resource_using_boto3

2. **Create Virtual Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

3. **Install the requires packages:**
   ```bash
   pip install -r requirements.txt


4. **Create an .env file with the following details:**
   ```bash
    Image_ID = ''
    Min_Count = ''
    Max_Count = ''
    Instance_Type = ''         
    Key_Name = ''       

## Interation with AWS EC2

1. **create an instance:**
   ```bash
    cd ec2
    python3 create_ec2.py
    
![alt text](image.png)

2. **get an instance details:**
   ```bash
    python3 instance_detail.py

![alt text](image-1.png)

3. **delete an instance:**
   ```bash
    python3 delete_instance.py

![alt text](image-2.png)

## Interation with AWS S3

1. **create an instance:**
   ```bash
    cd s3
    python3 create_s3.py

![alt text](image-3.png)

2. **retrieve bucket(s):**
   ```bash
    python3 retrieve_bucket.py

![alt text](image-4.png)

3. **upload file to bucket:**
   ```bash
    python3 upload_file_to_bucket.py

![alt text](image-5.png)

4. **download file from bucket:**
   ```bash
    python3 download_file_from_bucket.py

![alt text](image-6.png)

5. **delete bucket:**
   ```bash
    python3 delete_bucket.py

![alt text](image-7.png)

## Interation with AWS SQS

1. **create a queue:**
   ```bash
    cd sqs
    python3 create_sqs.py

![alt text](image-8.png)

2. **retrieve queue:**
   ```bash
    python3 retrieve_sqs.py

![alt text](image-9.png)

3. **delete queue:**
   ```bash
    python3 delete_sqs.py

