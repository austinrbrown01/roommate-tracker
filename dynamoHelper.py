import secrets
import boto3
import aws_creds
class dynamoDbHelper:
    def __init__(self):
        self.access_key = aws_creds.aws_access_key_id
        self.secret_access_key = aws_creds.aws_secret_access_key
        self.session = boto3.session.Session(aws_access_key_id=self.access_key, aws_secret_access_key=self.secret_access_key, region_name="us-west-2")
        self.dynamodb = self.session.client('dynamodb')

    def update_roommate_status(self, name, status):
        print("call to update_roommate_status with args: " + name + ", " + status)
        self.dynamodb.put_item(
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