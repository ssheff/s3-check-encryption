import boto3
from botocore.exceptions import ClientError
s3 = boto3.client('s3')
response = s3.list_buckets()

for bucket in response['Buckets']:
  try:
    isenc = s3.get_bucket_encryption(Bucket=bucket['Name'])
    rules = isenc['ServerSideEncryptionConfiguration']['Rules']
    print('Good job!. The bucket has: %s, Encryption: %s' % (bucket['Name'], rules))
  except ClientError as e:
    if e.response['Error']['Code'] == 'ServerSideEncryptionConfigurationNotFoundError':
      print('Not a good sign at all! The Bucket: %s, no server-side encryption' % (bucket['Name']))
    else:
      print("Hmmm, something with a bucket: %s, unexpected error: %s" % (bucket['Name'], e))
