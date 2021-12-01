import os
import requests
import json
import boto3

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from recipes.models import Recipe


class Command(BaseCommand):
    """
    Bakes out database output as json
    """
    def handle(self, *args, **kwargs):
        bucketName = "static.startribune.com"
        appPath = "news/projects/all/20191106-cookie-wars/data"
        fileName = "recipes.json"
        # bucketName = "strib-ig-photos"

        outputName = "assets/features/thomas/ig_photos.json"

        Key1 = "assets/features/thomas/ig_photos.json"
        output1 = "assets/features/thomas/old_ig_photos.json"

        local_path = "old_ig_photos.json"

        filename = "ig_photos.json"
        old_filename = "old_ig_photos.json"
        # url = "http://localhost:8000/api/ig_photos/photo/?format=json"
        url = "http://ig.internal.stribapps.com/api/ig_photos/photo/?format=json"

        # s3 = boto3.resource('s3')
        # try:
        #     s3.Bucket(bucketName).download_file(Key1)
        # except botocore.exceptions.ClientError as e:
        #     if e.response['Error']['Code'] == "404":
        #         print("The object does not exist.")
        #     else:
        #         raise

        s3 = boto3.client(
            's3',
            aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
            aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY')
        )
        s3.download_file(bucketName, Key1, local_path)

        self.stdout.write('Baking database to JSON...', ending="\n")
        resp = requests.get(url=url,)
        json_data = json.loads(resp.text)

        with open('%s' % filename, 'w') as outfile:
            json.dump(json_data, outfile)

        s3 = boto3.client(
            's3',
            aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
            aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY')
        )
        s3.upload_file(filename, bucketName, outputName)
        s3.upload_file(old_filename, bucketName, output1)
