import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('StudentsTable')

def lambda_handler(event, context):
    try:
        response = table.scan()
        students = response.get('Items', [])

        return {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "GET,OPTIONS"
            },
            "body": json.dumps(students)
        }

    except Exception as e:
        return {"statusCode": 500, "body": json.dumps({"error": str(e)})}
