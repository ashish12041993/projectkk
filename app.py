import boto3
import my changes ashish
ec2 = boto3.client('ec2')

def create_ec2_instance():
    try:
        response = ec2.run_instances(
            ImageId='ami-0abcdef1234567890',  
            InstanceType='t2.micro',          
            KeyName='aws',     
            MinCount=1,
            MaxCount=1,
            SecurityGroupIds=['sg-0123456789abcdef0'],  
            SubnetId='subnet-0123456789abcdef0',       
            TagSpecifications=[
                {
                    'ResourceType': 'instance',
                    'Tags': [
                        {'Key': 'Name', 'Value': 'MyBoto3Instance'}
                    ]
                }
            ]
        )
