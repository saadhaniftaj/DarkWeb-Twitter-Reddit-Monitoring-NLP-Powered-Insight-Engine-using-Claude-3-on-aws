import boto3
import json
import os

# Load credentials
AWS_REGION = "us-east-1"  # Change this based on your AWS Bedrock region
AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")
S3_BUCKET_NAME = "your-bucket-name"

# AWS Clients
s3_client = boto3.client("s3", aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_KEY)
bedrock_client = boto3.client("bedrock", region_name=AWS_REGION)

def analyze_with_claude():
    # Read Twitter data from S3
    response = s3_client.get_object(Bucket=S3_BUCKET_NAME, Key="twitter/twitter_data.json")
    twitter_data = json.loads(response["Body"].read().decode("utf-8"))

    # Prepare the AI model input
    input_text = "Analyze this data: " + json.dumps(twitter_data[:5])  # Sending first 5 tweets

    # Call Claude 3 Model on AWS Bedrock
    response = bedrock_client.invoke_model(
        modelId="anthropic.claude-3",  
        contentType="application/json",
        accept="application/json",
        body=json.dumps({"prompt": input_text})
    )

    # Parse response
    output = json.loads(response["body"].read().decode("utf-8"))
    print("AI Analysis:", output)

if __name__ == "__main__":
    analyze_with_claude()
