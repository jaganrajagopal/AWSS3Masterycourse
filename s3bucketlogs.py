import boto3
import os

s3 = boto3.client('s3')

def lambda_handler(event, context):
    # Bucket and file name from the Lambda event trigger
    print(event)
    print("****")
    print(context)
    bucket_name = event['bucketname']
    file_key = 'appslogs/log.txt'
    
    # Download the log file from S3
    log_file = '/tmp/log.txt'
    s3.download_file(bucket_name, file_key, log_file)
    #s3.meta.client.download_file(bucket_name, file_key, log_file)
    
    # Initialize aggregation variables
    error_count = 0
    info_count = 0
    
    # Process the log file
    with open(log_file, 'r') as f:
        for line in f:
            # Basic parsing logic based on assumed log format
            parts = line.split(';')  # Adjust this based on your log format
            log_level = parts[1]  # Assuming second part is log level
            #print(parts)
            print("*****")
            print(log_level)
            # Filtering and aggregation
            print("*****Error****")
            print (log_level.find("ERROR"))
            if log_level.find("ERROR") == 1:
                error_count += 1
            elif log_level.find("INFO")== 1:
                info_count += 1
    
    # Example aggregation result
    print(f"INFO logs: {info_count}, ERROR logs: {error_count}")
    
    # Extend this script to forward these results to another AWS service
    # or write an aggregated result back to S3 as needed.
    
    return {
        'statusCode': 200,
        'body': f"Processed log file {file_key} with {info_count} INFO logs and {error_count} ERROR logs."
    }
