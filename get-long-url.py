import json
import boto3

ddb = boto3.resource('dynamodb', region_name = 'us-east-1').Table('url-shortener')

def lambda_handler(event, context):
    short_url = event.get('short_url')
    try:
        url_item = ddb.get_item(Key={'short_url': short_url})
        long_url = url_item.get('Item').get('long_url')
        return {
            'statusCode': 200,
            'headers': {
                "Content-Type" : "application/json",
                "Access-Control-Allow-Headers" : "Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token",
                "Access-Control-Allow-Methods" : "OPTIONS,POST,GET",
                "Access-Control-Allow-Credentials" : True,
                "Access-Control-Allow-Origin" : "*",
                "X-Requested-With" : "*"
            },
            'body': json.dumps({ "long_url": long_url })
        }
        
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error_msg':'Short Token not found'})
        }
