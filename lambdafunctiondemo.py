import json

def lambda_handler(event, context):
    # TODO implement
    print('For s3 Object created event has been triggered by jagan via S3 event')
    return {
        'statusCode': 200,
        'body': json.dumps('Trigger Lambda via Active Mq ')
    }
