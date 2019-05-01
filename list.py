#!/usr/bin/python3
import os
import boto3
import boto3.session
import time
import datetime

session = boto3.session.Session(profile_name='usj23')

endpoint = 'https://110.74.179.150:443/'
s3 = session.resource(service_name='s3', endpoint_url=endpoint, verify=False)


for o in s3.Bucket('rasp').objects.all():
    print("Key: " + o.key)
    print("Size: " + str(o.size))
    print("Time: " + str(o.last_modified))
    response = s3.Object('rasp', o.key ).get()
    #data = response['Body'].read()
    metadata = response['Metadata']
    print("Metadata: %s" % (metadata))

