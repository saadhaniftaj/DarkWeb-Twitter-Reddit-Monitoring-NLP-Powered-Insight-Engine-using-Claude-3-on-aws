import requests
import json
import boto3
import os

# Load credentials
AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")
S3_BUCKET_NAME = "your-bucket-name"

# AWS S3 Client
s3_client = boto3.client("s3", aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_KEY)

def fetch_reddit_data():
    url = "https://www.reddit.com/r/all/new.json?limit=100"
    headers = {"User-Agent": "Mozilla/5.0"}
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        save_to_s3("reddit/reddit_data.json", data)
        print("Reddit data saved successfully!")
    else:
        print("Error fetching Reddit data:", response.text)

def save_to_s3(file_name, data):
    s3_client.put_object(Bucket=S3_BUCKET_NAME, Key=file_name, Body=json.dumps(data))

if __name__ == "__main__":
    fetch_reddit_data()
