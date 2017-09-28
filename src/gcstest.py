#coding: utf-8

import os
if os.environ.get("GCLOUD_PROJECT") is None: 
    os.environ["GCLOUD_PROJECT"] = "cyberagent-194" #prague-dev

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/container/credentials.json"

from googleapiclient import discovery
from oauth2client.client import GoogleCredentials
credentials = GoogleCredentials.get_application_default()
compute = discovery.build('compute', 'v1', credentials=credentials)

from google.cloud import storage

bucket_name = "prague-misc"
client = storage.Client()
print(list(client.list_buckets()))

bucket = client.get_bucket(bucket_name)
for blob in bucket.list_blobs():
    print(blob)

n = 0
for i in range(1000000000):
    n += i
print(n)


