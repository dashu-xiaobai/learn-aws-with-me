import boto3

# Initialize client
s3 = boto3.client('s3', region_name='us-east-2')

# List buckets
bucket_resp = s3.list_buckets()

# Print out bucket names
for bucket in bucket_resp['Buckets']:
    print(bucket['Name'])


