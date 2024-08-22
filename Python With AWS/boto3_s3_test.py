import boto3

s3_client = boto3.client('s3')

response = s3_client.list_buckets()


buckets = response['Buckets']
for bucket in buckets:
    print(bucket['Name'])