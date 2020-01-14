# coding: utf-8
import boto3
session = boto3.Session(profile_name='pythonAutomation')
s3 = session.resource('s3')
import boto3
session = boto3.Session(profile_name='default')
s3 = session.resource('s3')
bucket = s3.create_bucket(Bucket='melshmanvideolyzervideos')
bucket = s3.create_bucket(Bucket='melshmanvideolyzervideos2', LocationConstraint=session.region_name)
session.region_name
session.region_name
from pathlib import Path
get_ipython().run_line_magic('ls', '')
get_ipython().run_line_magic('pwd', '')
get_ipython().run_line_magic('ls', './*.mp4')
pathname = './familtyCelabrationVideo.mp4'
pathname
path = Path(pathname).expanduser().resolve()
path
print(path)
bucket.upload_file(str(path), str(path.name))
path.name
bucket.name
rekognition_client = session.client('rekognition')
response = rekognition_client.start_label_detection(Video={'S3Object': { 'Bucket': bucket.name, 'Name': path.name}})
rekognition_client = session.client('rekognition')
response = rekognition_client.start_label_detection(Video={'S3Object': { 'Bucket': bucket.name, 'Name': path.name}})
response
response['JobId']
job_id = response['JobId']
result = rekognition_client.get_label_detection(JobId=job_id)
result
result(keys)
result.keys()
result['JobStatus']
result['VideoMetadata']
result['LabelModelVersion']
result['ResponseMetadata']
len(result['Labels'])
result['Labels']
