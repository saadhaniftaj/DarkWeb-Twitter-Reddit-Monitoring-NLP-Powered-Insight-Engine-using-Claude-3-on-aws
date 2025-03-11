import requests
import json
import boto3
import os

# Load credentials
TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")
S3_BUCKET_NAME = "your-bucket-name"

# AWS S3 Client
s3_client = boto3.client("s3", aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_KEY)

def fetch_twitter_data():
    url = "https://api.twitter.com/2/tweets/search/recent?query=-is:retweet&max_results=100"
    headers = {"Authorization": f"Bearer {TWITTER_API_KEY}"}
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        save_to_s3("twitter/twitter_data.json", data)
        print("Twitter data saved successfully!")
    else:
        print("Error fetching Twitter data:", response.text)

def save_to_s3(file_name, data):
    s3_client.put_object(Bucket=S3_BUCKET_NAME, Key=file_name, Body=json.dumps(data))
    
if __name__ == "__main__":
    fetch_twitter_data()
