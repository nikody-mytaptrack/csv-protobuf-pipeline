import boto3
import pandas
import os
import json
import logging
import sys
from sagemaker.amazon.common import numpy_to_record_serializer
logger = logging.getLogger()
logger.setLevel(logging.INFO)

s3 = boto3.resource('s3')
client = boto3.client('s3')
serializer = numpy_to_record_serializer()

def toProto(event, context):
    try:
        logger.info(event)
        s3Record = event['Records'][0]['s3']
        bucket = s3Record['bucket']['name']
        key = s3Record['object']['key']
        
        logger.info('Getting original object')
        origin = s3.Object(bucket, key)
        logger.info('Object retrieved')
        logger.info(origin)

        logger.info('Getting tags')
        tagging = client.get_object_tagging(Bucket=bucket,Key=key)
        logger.info('Tags retrieved')
        logger.info(tagging['TagSet'])
        
        tags = ''
        for tag in tagging['TagSet']:
            tags += tag['Key'] + '=' + tag['Value'] + ','

        tags = tags[0: len(tags) - 1]

        logger.info('Downloading file')
        localFile = '/tmp/' + str(key).replace('/', '-')
        origin.download_file(localFile)
        
        logger.info('Converting with pandas')
        data = pandas.read_csv(localFile, delimiter=',')
        ndarray = data.values
        buffer = serializer(ndarray)
        
        logger.info('Uploading file')
        outKey = os.environ['train_data_prefix'] + key
        outBucket = os.environ['train_data_bucket']
        s3Object = s3.Object(outBucket, outKey)
        kms = os.environ['kms']
        if kms is '' :
            s3Object.put(Body=buffer, Tagging=tags)
        else :
            s3Object.put(Body=buffer, Tagging=tags, ServerSideEncryption='aws:kms')

        logger.info('Deleting old file');
        s3.Object(bucket, key).delete()
    except:
        logger.error(sys.exc_info()[0])
        raise
