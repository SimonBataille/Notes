import boto3

# Create an S3 client
# Remember to create access key and secret key in minio
s3 = boto3.client(
    service_name='s3',
    endpoint_url='http://localhost:9000',
    aws_access_key_id='NvMp7Z8HrnW3DWVSr6oH',
    aws_secret_access_key='sGHDBtevnv0nNlHllQciYRkjyrji9L93Z9BZn7uK'
    )

# Call S3 to list current buckets
# response = s3.list_buckets()
# print(response)

# Test upload file
# s3.upload_file('test.txt', 'isc', 'bucket_test.txt')

# Test download file
# s3.download_file('isc', 'bucket_test.txt', 'test_download.txt')

# Test list file
response = s3.list_objects(Bucket='isc')
for content in response['Contents']:
    print(content['Key'])

# Test delete file
# s3.delete_object(Bucket='isc', Key='bucket_test.txt')