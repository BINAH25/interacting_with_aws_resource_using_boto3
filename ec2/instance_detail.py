import boto3

ec2 = boto3.client('ec2')

# Describe the instances
response = ec2.describe_instances()
if response:
    # Extract relevant details
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            instance_type = instance['InstanceType']
            public_ip = instance.get('PublicIpAddress', 'No public IP')
            # private_ip = instance['PrivateIpAddress','No private IP']
            state = instance['State']['Name']
            tags = instance.get('Tags', [])
            
            # You can also extract specific tag names if needed
            instance_name = 'No name'
            for tag in tags:
                if tag['Key'] == 'Name':
                    instance_name = tag['Value']

            # Print the details
            print(f"Instance ID: {instance_id}")
            print(f"Instance Name: {instance_name}")
            print(f"Instance Type: {instance_type}")
            print(f"Public IP: {public_ip}")
            # print(f"Private IP: {private_ip}")
            print(f"State: {state}")
            print("-" * 40)
else:
    print("no instances found")