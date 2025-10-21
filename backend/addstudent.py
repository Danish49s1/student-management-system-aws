import json
import boto3
import uuid

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('StudentsTable')  # Replace with your DynamoDB table name

def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])
        name = body.get('name')
        age = body.get('age')
        course = body.get('course')

        if not all([name, age, course]):
            return {"statusCode": 400, "body": json.dumps({"error": "Missing fields"})}

        student_id = str(uuid.uuid4())

        table.put_item(
            Item={
                'studentId': student_id,
                'name': name,
                'age': int(age),
                'course': course
            }
        )

        return {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "POST,OPTIONS"
            },
            "body": json.dumps({
                "message": "Student added successfully",
                "studentId": student_id
            })
        }

    except Exception as e:
        return {"statusCode": 500, "body": json.dumps({"error": str(e)})}
