


response = client.create_launch_configuration(
    LaunchConfigurationName='LC-Notifon',
    ImageId=img.id,
    KeyName=key_name,
    SecurityGroups=[
        sg,
    ],
    UserData='yum install httpd php mysql php-mysql -y',
    InstanceType='t2.micro',
        InstanceMonitoring={
        'Enabled': False
    },
)


# create autoscaling group
response = client.create_auto_scaling_group(
    AutoScalingGroupName='NotifonASgroup',
    LaunchConfigurationName='LC-Notifon',
    MinSize=1,
    MaxSize=4,
    DesiredCapacity=1,
    DefaultCooldown=10,
)


response = client.put_scaling_policy(
    AutoScalingGroupName='NotifonASgroup',
    PolicyName='scale-up',
    PolicyType='SimpleScaling',
    AdjustmentType='ChangeInCapacity',
    MinAdjustmentMagnitude=1,
    ScalingAdjustment=1,
    Cooldown=10,
)


# Create AS based on Launch LaunchConfiguration

# Create AS policies

# execute AS Policies (See )
import boto3
session = boto3.Session(profile_name='melshman')
as_client = session.client('autoscaling')

as_client.execute_policy(AutoScalingGroupName='NotifonASgroup', PolicyName='scale-up')



# # full create autoscaling group template
# response = client.create_auto_scaling_group(
#     AutoScalingGroupName='ASG_Notifon',
#     LaunchConfigurationName='string',
#     LaunchTemplate={
#         'LaunchTemplateId': 'string',
#         'LaunchTemplateName': 'string',
#         'Version': 'string'
#     },
#     MixedInstancesPolicy={
#         'LaunchTemplate': {
#             'LaunchTemplateSpecification': {
#                 'LaunchTemplateId': 'string',
#                 'LaunchTemplateName': 'string',
#                 'Version': 'string'
#             },
#             'Overrides': [
#                 {
#                     'InstanceType': 'string',
#                     'WeightedCapacity': 'string'
#                 },
#             ]
#         },
#         'InstancesDistribution': {
#             'OnDemandAllocationStrategy': 'string',
#             'OnDemandBaseCapacity': 123,
#             'OnDemandPercentageAboveBaseCapacity': 123,
#             'SpotAllocationStrategy': 'string',
#             'SpotInstancePools': 123,
#             'SpotMaxPrice': 'string'
#         }
#     },
#     InstanceId='string',
#     MinSize=123,
#     MaxSize=123,
#     DesiredCapacity=123,
#     DefaultCooldown=123,
#     AvailabilityZones=[
#         'string',
#     ],
#     LoadBalancerNames=[
#         'string',
#     ],
#     TargetGroupARNs=[
#         'string',
#     ],
#     HealthCheckType='string',
#     HealthCheckGracePeriod=123,
#     PlacementGroup='string',
#     VPCZoneIdentifier='string',
#     TerminationPolicies=[
#         'string',
#     ],
#     NewInstancesProtectedFromScaleIn=True|False,
#     LifecycleHookSpecificationList=[
#         {
#             'LifecycleHookName': 'string',
#             'LifecycleTransition': 'string',
#             'NotificationMetadata': 'string',
#             'HeartbeatTimeout': 123,
#             'DefaultResult': 'string',
#             'NotificationTargetARN': 'string',
#             'RoleARN': 'string'
#         },
#     ],
#     Tags=[
#         {
#             'ResourceId': 'string',
#             'ResourceType': 'string',
#             'Key': 'string',
#             'Value': 'string',
#             'PropagateAtLaunch': True|False
#         },
#     ],
#     ServiceLinkedRoleARN='string',
#     MaxInstanceLifetime=123
# )



# # put_scaling_policy(**kwargs)
# # Creates or updates a scaling policy for an Auto Scaling group. To update an existing scaling policy, use the existing policy name and set the parameters to change. Any existing parameter not changed in an update to an existing policy is not changed in this update request.

# # For more information about using scaling policies to scale your Auto Scaling group automatically, see Dynamic Scaling in the Amazon EC2 Auto Scaling User Guide .

# # See also: AWS API Documentation

# # Request Syntax

# response = client.put_scaling_policy(
#     AutoScalingGroupName='string',
#     PolicyName='scale-up',
#     PolicyType='SimpleScaling',
#     AdjustmentType='ChangeInCapacity',
#     MinAdjustmentMagnitude=1,
#     ScalingAdjustment=1,
#     Cooldown=10,
# )



# # describe_policies(**kwargs)
# # Describes the policies for the specified Auto Scaling group.

# # See also: AWS API Documentation

# # Request Syntax

# response = client.describe_policies(
#     AutoScalingGroupName='string',
#     PolicyNames=[
#         'string',
#     ],
#     PolicyTypes=[
#         'string',
#     ],
#     NextToken='string',
#     MaxRecords=123
)


# # execute_policy(**kwargs)
# # Executes the specified policy.
# response = client.execute_policy(
#     AutoScalingGroupName='string',
#     PolicyName='string',
#     HonorCooldown=True|False,
#     MetricValue=123.0,
#     BreachThreshold=123.0
# )




# # create_launch_configuration(**kwargs)
# # Creates a launch configuration.

# # If you exceed your maximum limit of launch configurations, the call fails. For information about viewing this limit, see DescribeAccountLimits . For information about updating this limit, see Amazon EC2 Auto Scaling Limits in the Amazon EC2 Auto Scaling User Guide .

# # For more information, see Launch Configurations in the Amazon EC2 Auto Scaling User Guide .

# # See also: AWS API Documentation

# # Request Syntax

# response = client.create_launch_configuration(
#     LaunchConfigurationName='string',
#     ImageId='string',
#     KeyName='string',
#     SecurityGroups=[
#         'string',
#     ],
#     ClassicLinkVPCId='string',
#     ClassicLinkVPCSecurityGroups=[
#         'string',
#     ],
#     UserData='string',
#     InstanceId='string',
#     InstanceType='string',
#     KernelId='string',
#     RamdiskId='string',
#     BlockDeviceMappings=[
#         {
#             'VirtualName': 'string',
#             'DeviceName': 'string',
#             'Ebs': {
#                 'SnapshotId': 'string',
#                 'VolumeSize': 123,
#                 'VolumeType': 'string',
#                 'DeleteOnTermination': True|False,
#                 'Iops': 123,
#                 'Encrypted': True|False
#             },
#             'NoDevice': True|False
#         },
#     ],
#     InstanceMonitoring={
#         'Enabled': True|False
#     },
#     SpotPrice='string',
#     IamInstanceProfile='string',
#     EbsOptimized=True|False,
#     AssociatePublicIpAddress=True|False,
#     PlacementTenancy='string'
# )



# # create_auto_scaling_group(**kwargs)
# # Creates an Auto Scaling group with the specified name and attributes.

# # If you exceed your maximum limit of Auto Scaling groups, the call fails. For information about viewing this limit, see DescribeAccountLimits . For information about updating this limit, see Amazon EC2 Auto Scaling Limits in the Amazon EC2 Auto Scaling User Guide .

# # See also: AWS API Documentation

# # Request Syntax

# response = client.create_auto_scaling_group(
#     AutoScalingGroupName='string',
#     LaunchConfigurationName='string',
#     LaunchTemplate={
#         'LaunchTemplateId': 'string',
#         'LaunchTemplateName': 'string',
#         'Version': 'string'
#     },
#     MixedInstancesPolicy={
#         'LaunchTemplate': {
#             'LaunchTemplateSpecification': {
#                 'LaunchTemplateId': 'string',
#                 'LaunchTemplateName': 'string',
#                 'Version': 'string'
#             },
#             'Overrides': [
#                 {
#                     'InstanceType': 'string',
#                     'WeightedCapacity': 'string'
#                 },
#             ]
#         },
#         'InstancesDistribution': {
#             'OnDemandAllocationStrategy': 'string',
#             'OnDemandBaseCapacity': 123,
#             'OnDemandPercentageAboveBaseCapacity': 123,
#             'SpotAllocationStrategy': 'string',
#             'SpotInstancePools': 123,
#             'SpotMaxPrice': 'string'
#         }
#     },
#     InstanceId='string',
#     MinSize=123,
#     MaxSize=123,
#     DesiredCapacity=123,
#     DefaultCooldown=123,
#     AvailabilityZones=[
#         'string',
#     ],
#     LoadBalancerNames=[
#         'string',
#     ],
#     TargetGroupARNs=[
#         'string',
#     ],
#     HealthCheckType='string',
#     HealthCheckGracePeriod=123,
#     PlacementGroup='string',
#     VPCZoneIdentifier='string',
#     TerminationPolicies=[
#         'string',
#     ],
#     NewInstancesProtectedFromScaleIn=True|False,
#     LifecycleHookSpecificationList=[
#         {
#             'LifecycleHookName': 'string',
#             'LifecycleTransition': 'string',
#             'NotificationMetadata': 'string',
#             'HeartbeatTimeout': 123,
#             'DefaultResult': 'string',
#             'NotificationTargetARN': 'string',
#             'RoleARN': 'string'
#         },
#     ],
#     Tags=[
#         {
#             'ResourceId': 'string',
#             'ResourceType': 'string',
#             'Key': 'string',
#             'Value': 'string',
#             'PropagateAtLaunch': True|False
#         },
#     ],
#     ServiceLinkedRoleARN='string',
#     MaxInstanceLifetime=123
# )





# get all security SecurityGroups
response = client.describe_security_groups(
    Filters=[
        {
            'Name': 'string',
            'Values': [
                'string',
            ]
        },
    ],
    GroupIds=[
        'string',
    ],
    GroupNames=[
        'string',
    ],
    DryRun=True|False,
    NextToken='string',
    MaxResults=123
)




# find default VPC
#filters = [{'Name':'tag:Name', 'Values':['VPN01', 'VPN02']}]
vpcs = list(ec2.vpcs)
for vpc in vpcs:
    response = ec2_client.describe_vpcs(
        VpcIds=[
            vpc.id,
        ]
    )
    print(json.dumps(response, sort_keys=True, indent=4))

