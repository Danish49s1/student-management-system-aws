import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('StudentsTable')

def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])
        student_id = body.get('studentId')

        if not student_id:
            return {"statusCode": 400, "body": json.dumps({"error": "Missing studentId"})}

        table.delete_item(Key={'studentId': student_id})

        return {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "DELETE,OPTIONS"
            },
            "body": json.dumps({"message": "Student deleted successfully"})
        }

    except Exception as e:
        return {"statusCode": 500, "body": json.dumps({"error": str(e)})}
