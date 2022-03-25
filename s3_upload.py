# import requests
# import csv
# import json
import  boto3
from auth import ACCESS_KEY,SECRET_KEY

def pushS3():
    ''' pushing data to S3 bucket'''
    client=boto3.client('s3',aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
    
    client.create_bucket(Bucket='final-project-late-table')
    with open("/home/yunus/is_late_table.csv","rb") as f:
        client.upload_fileobj(f,"final-project-late-table","is_late_table.csv")

    print("Upload Completed")
