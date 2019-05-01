#!/usr/bin/python3
import os
import boto3
import boto3.session
import time
import datetime

session = boto3.session.Session(profile_name='usj23')

endpoint = 'https://110.74.179.150:443/'
s3 = session.resource(service_name='s3', endpoint_url=endpoint, verify=False)

#for bucket in s3.buckets.all():
#    print(bucket.name)
#
#bucket = s3.Bucket('rasp').create()
#
#print('created new bucket')
#for bucket in s3.buckets.all():
#    print(bucket.name)

def create_log():
    nowtime = datetime.datetime.now().strftime('%Y-%m-%d-%H:%M:%S')
    print(nowtime)
    #'''
    f= open("/tmp/s3upload","w+")
    for i in range(100):
        f.write("testing for home s3 script %d\n" % (i+1))
    f.close()
    objMetadata = {'animal' : 'snow leopard', 'city' : 'liverpool', 'food' : 'durian'}
    filename = '/tmp/s3upload'
    obj = s3.Object('rasp', nowtime )
    obj.upload_file(filename, ExtraArgs={"Metadata": objMetadata})
    #'''

create_log()
