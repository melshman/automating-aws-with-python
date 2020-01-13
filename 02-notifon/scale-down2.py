# coding: utf-8
import boto3
session = boto3.Session(profile_name='default')
as_client = session.client('autoscaling')

as_client.execute_policy(AutoScalingGroupName='NotifonASgroup', PolicyName='scale-down2')
