# ec2 instance create -Tim

# coding: utf-8
import boto3
session = boto3.Session(profile_name='melshman')
ec2 = session.resource('ec2')

key_name = 'pyautomation_test_key'
key_path = key_name + '.pem'

# Use if using existing keypair
key = ec2.KeyPair(key_name)


# # Use to create (note: can't use if keypair name already exists)
# key = ec2.create_key_pair(KeyName=key_name)

# # Can only get the key.key_material when you create the key... never again
# key.key_material


# # write key_material to file
# with open(key_path, 'w') as key_file:
#     key_file.write(key.key_material)

#change permissions on key
get_ipython().run_line_magic('ls', '-l pyautomation_test_key.pem')
import os, stat
os.chmod(key_path, stat.S_IRUSR | stat.S_IWUSR)
get_ipython().run_line_magic('ls', '-l pyautomation_test_key.pem')

# # get images - takes LONG TIME!
# ec2.images.filter(Owners=['amazon'])
# list(ec2.images.filter(Owners=['amazon']))
# len(list(ec2.images.filter(Owners=['amazon'])))

# get the image id from EC2 Console
img = ec2.Image('ami-062f7200baf2fa504')
ami_name = img.name
ami_id = img.image_id
# 'amzn2-ami-hvm-2.0.20191217.0-x86_64-gp2'

# ec2_apse2 = session.resource('ec2', region_name='ap-southeast-2')
# img_apse2 = ec2_apse2.Image('ami-922914f7')
# img_apse2.name
# img.name

# find ami with ami_name
filters = [{'Name': 'name', 'Values': [ami_name]}]
list(ec2.images.filter(Owners=['amazon'], Filters=filters))
img2=list(ec2.images.filter(Owners=['amazon'], Filters=filters))[0]
img2.name
ami_name2 = img2.name
img2.image_id
ami_id2 = img2.image_id
# 'ami-062f7200baf2fa504'
# list(ec2_apse2.images.filter(Owners=['amazon'], Filters=filters))

img
key
instances = ec2.create_instances(ImageId=img.id, MinCount=1, MaxCount=1, InstanceType='t2.micro', KeyName=key.key_name)
instances
ec2.Instance(id='i-0f0733eac277c029c')
inst = instances[0]

dir(inst)
inst
inst.public_dns_name
inst.public_ip_address
inst.private_ip_address
inst.network_interfaces

inst.wait_until_running()

# Reload the instance attributes after running
inst.reload()

inst
inst.public_dns_name
inst.public_ip_address
inst.private_ip_address
inst.network_interfaces

# Look up the security group
inst.security_groups
inst.security_groups[0]['GroupId']

# test termination of instance and then re-create
# inst.terminate()
# instances = ec2.create_instances(ImageId=img.id, MinCount=1, MaxCount=1, InstanceType='t2.micro', KeyName=key.key_name)
# inst= instances[0]
# inst.reload()
# inst
# inst.public_dns_name
# inst.public_ip_address
# inst.private_ip_address
# inst.network_interfaces


# Authorize incoming connections from our public IP address, on port 22 (the port SSH uses)
# update with current IP address - google 'what is my ip address'
# will get error if already exists
sg = ec2.SecurityGroup(inst.security_groups[0]['GroupId'])
sg.authorize_ingress(IpPermissions=[{'FromPort': 22, 'ToPort': 22, 'IpProtocol': 'TCP', 'IpRanges': [{'CidrIp': '208.185.7.130/32'}]}])
sg.authorize_ingress(IpPermissions=[{'FromPort': 80, 'ToPort': 80, 'IpProtocol': 'TCP', 'IpRanges': [{'CidrIp': '0.0.0.0/0'}]}])

# use dns_name in order to ssh into instance
# ssh -i key_path ec2
inst.public_dns_name
# get_ipython().run_line_magic('history', '')

#
session = boto3.Session()
ec2_client = session.client('ec2')
sg_list = ec2_client.describe_security_groups()

# auto scallilng group creation based on existing instance ID
as_client = session.client('autoscaling')

response = as_client.create_launch_configuration(
    LaunchConfigurationName='LC-Notifon',
    ImageId=img.id,
    KeyName=key_name,
    SecurityGroups=[
        'sg-014f1c59e1ef2149e',
    ],
    UserData='yum install httpd php mysql php-mysql -y',
    InstanceType='t2.micro',
        InstanceMonitoring={
        'Enabled': False
    },
)

# create autoscaling group
# Need to figure out how to get the instances associated with autoscaling group
# THen get instance id, dns so ssh to it.

### Need to figure out how to get list of VPCs ###
### Need to figure out how to select the Default VPC from List ###
### Need to figure out how to get list of subnets in a VPC
### Need to figure out how to select one of the subnets to use


response = as_client.create_auto_scaling_group(
AutoScalingGroupName='NotifonASgroup',
LaunchConfigurationName='LC-Notifon',
# VPCZoneIdentifier is subnet_id
VPCZoneIdentifier='subnet-019057524bbbc7f31',
MinSize=1,
MaxSize=4,
DesiredCapacity=1,
DefaultCooldown=10,
)

response = as_client.put_scaling_policy(
    AutoScalingGroupName='NotifonASgroup',
    PolicyName='scale-up',
    PolicyType='SimpleScaling',
    AdjustmentType='ChangeInCapacity',
    ScalingAdjustment=1,
    Cooldown=10,
)

response = as_client.put_scaling_policy(
    AutoScalingGroupName='NotifonASgroup',
    PolicyName='scale-down2',
    PolicyType='SimpleScaling',
    AdjustmentType='ChangeInCapacity',
    ScalingAdjustment=-1,
    Cooldown=10,
)

# update so you can ssh into instance
# had to get sg_id from console after instance created (See above notes - todo)
sg = ec2.SecurityGroup('sg-014f1c59e1ef2149e')
sg.authorize_ingress(IpPermissions=[{'FromPort': 22, 'ToPort': 22, 'IpProtocol': 'TCP', 'IpRanges': [{'CidrIp': '208.185.7.130/32'}]}])




# scale up test
as_client.execute_policy(AutoScalingGroupName='NotifonASgroup', PolicyName='scale-up')

# scale down test
as_client.execute_policy(AutoScalingGroupName='NotifonASgroup', PolicyName='scale-down2')

