from http import client
from urllib import response
import boto3

s3_client = boto3.resource('s3')

'''bucket creation'''
response = s3_client.create_bucket(
    ACL='private',
    Bucket='s3-bucket-801284',
    CreateBucketConfiguration={
        'LocationConstraint': 'ap-south-1'
    }
)

'''upload a file into s3 bucket'''
s3_client.meta.client.upload_file('sasi kumar.txt', 's3-bucket-801284', 'sasi kumar.txt')


'''bucket creation using keys'''
s3_client = boto3.client(service_name='s3', region_name='ap-south-1',
    aws_access_key_id='AKIAYRRDYOCOSM5L4DMO',
    aws_secret_access_key='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')
response = s3_client.create_bucket(
    ACL='private',
    Bucket='s3-bucket-80128424',
    CreateBucketConfiguration={
        'LocationConstraint': 'ap-south-1'
    }    
)


'''upload file'''
s3_client = boto3.resource('s3')
s3_client.meta.client.upload_file('sasi kumar.txt', 's3-bucket-80128424', 'sasi kumar.txt')


'''delete bucket'''
response = s3_client.delete_bucket(
    Bucket='s3-bucket-801284',
    ExpectedBucketOwner='587411779741'
)


'''download file'''
s3_client = boto3.resource('s3')
s3_client.meta.client.download_file('s3-bucket-80128424', 'sasi kumar.txt', 'hello.txt')


'''read file'''
s3_client = boto3.resource('s3')
bucket = s3_client.Bucket('s3-bucket-80128424')
for obj in bucket.objects.all():
    key = obj.key
    body = obj.get()['Body'].read()
print(body)

