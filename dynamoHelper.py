import secrets
import boto3
import aws_creds
access_key = aws_creds.aws_access_key_id
secret_access_key = aws_creds.aws_secret_access_key
session = boto3.session.Session(aws_access_key_id=access_key, aws_secret_access_key=secret_access_key, region_name="us-west-2")

dynamodb = boto3.resource('dynamodb', region='us-west-2')

table = dynamodb.Table('roommate-status')

print(table.creation_date_time)