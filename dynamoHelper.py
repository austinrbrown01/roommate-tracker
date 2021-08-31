import secrets
import boto3
import aws_creds
access_key = aws_creds.aws_access_key_id
secret_access_key = aws_creds.aws_secret_access_key
session = boto3.session.Session(aws_access_key_id=access_key, aws_secret_access_key=secret_access_key, region_name="us-west-2")

dynamodb = session.client('dynamodb')

def update_roommate_status(name, status):
    dynamodb.put_item(
        TableName = 'roommate-status',
        Item={
            'name': {
                'S': name
            },
            'status': {
                'S': status
            }
        }
    )