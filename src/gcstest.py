#coding: utf-8
from google.cloud import storage

bucket_name = "prague-misc"
client = storage.Client()
print(list(client.list_buckets()))

bucket = client.get_bucket(bucket_name)
for blob in bucket.list_blobs():
    print(blob)
