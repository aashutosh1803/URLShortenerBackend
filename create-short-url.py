import json
import boto3
import random

ddb = boto3.resource('dynamodb', region_name = 'us-east-1').Table('url-shortener')
token_length = 6

def generate_short_url():
    alphaNumeric = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
        'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
        'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
        'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
    ]
    short_url = ''
    for i in range(0, (token_length)):
        short_url += random.choice(alphaNumeric)
    return short_url
    
def lambda_handler(event, context):
    long_url = json.loads(event.get('body')).get('long_url')
    short_url = generate_short_url()
    unique_short_url = True
    
    while unique_short_url:
        try:
            response = ddb.put_item(
                Item={
                    'short_url': short_url,
                    'long_url': long_url,
                },
                ConditionExpression = "attribute_not_exists(short_url)",
            )
            break
        except Exception as e:
            short_url = generate_short_url()
        
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
        'body': json.dumps({ "short_url": short_url })
    }
