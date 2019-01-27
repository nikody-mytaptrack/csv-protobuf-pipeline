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
serializer = numpy_to_record_serializer()

def toProto(event, context):
    try:
        logger.info(event)
        s3Record = event['Records'][0]['s3']
        bucket = s3Record['bucket']['name']
        key = s3Record['object']['key']
        
        localFile = '/tmp/' + str(key).replace('/', '-')
        s3.Bucket(bucket).download_file(key, localFile)
        data = pandas.read_csv(localFile, delimiter=',')
        ndarray = data.values
        buffer = serializer(ndarray)
        outKey = os.environ['train_data_prefix'] + key
        outBucket = os.environ['train_data_bucket']
        s3.Bucket(outBucket).Object(outKey).upload_fileobj(buffer)
        s3.Object(bucket, key).delete()
    except:
        logger.error(sys.exc_info()[0])
        raise
