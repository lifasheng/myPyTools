

# refer to https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html

import boto3
s3 = boto3.resource('s3')

bucket = "testBucket"
src_file = "00761403-5410-4C87-8119-F5487C9A997A/1580150027566-4711804227000"
dst_file = "00761403-5410-4C87-8119-F5487C9A997A.es_US/1580150027566-4711804227000"

copy_source = {
    'Bucket': bucket,
    'Key': src_file
}
s3.meta.client.copy(copy_source, bucket, dst_file)

