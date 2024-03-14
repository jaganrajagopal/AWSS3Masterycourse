import boto3
from datetime import datetime

s3 = boto3.client('s3')
bucket_name = 'awstrainingwithjagandemo'  # Replace with your bucket name

def lambda_handler(event, context):
    # Simulate log collection; replace this with your actual log collection logic
    logs = collect_logs(event)
    print("inside the lambda handler")
    # Generate a unique file name
    file_name = f"logs-{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.txt"
    
    # Save logs to S3
    s3.put_object(Bucket=bucket_name, Key=file_name, Body=logs)
    
    return {
        'statusCode': 200,
        'body': f"Successfully uploaded logs to {bucket_name}/{file_name}"
    }

def collect_logs(event):
    # Placeholder for log collection logic; adjust based on your log source
    # For example, if logs are passed directly to Lambda, you might just return `event`
    return str(event)  # Convert event (log data) to string, if not already
