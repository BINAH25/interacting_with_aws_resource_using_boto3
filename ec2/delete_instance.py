import boto3

# Create an EC2 client
ec2 = boto3.client('ec2')

# Describe instances
response = ec2.describe_instances()

# Loop through reservations and instances to get the Instance IDs
instance_ids = []
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        instance_ids.append(instance['InstanceId'])

# Print the Instance IDs
print("Instance IDs to delete:")
for instance_id in instance_ids:
    print(instance_id)

# Terminate instances
ec2.terminate_instances(InstanceIds=instance_ids)

print(f"Terminating instances: {instance_ids}")
