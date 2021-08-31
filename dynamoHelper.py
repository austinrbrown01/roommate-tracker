import boto3

dynamodb = boto3.resouce('dynamodb')

table = dynamodb.Table('roommate-status')

print(table.creation_date_time)