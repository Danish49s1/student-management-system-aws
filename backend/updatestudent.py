import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('StudentsTable')

def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])
        student_id = body.get('studentId')
        name = body.get('name')
        age = body.get('age')
        course = body.get('course')

        if not student_id:
            return {"statusCode": 400, "body": json.dumps({"error": "Missing studentId"})}

        update_expression = "SET "
        expression_values = {}

        if name:
            update_expression += "name = :n, "
            expression_values[":n"] = name
        if age:
            update_expression += "age = :a, "
            expression_values[":a"] = int(age)
        if course:
            update_expression += "course = :c, "
            expression_values[":c"] = course

        update_expression = update_expression.rstrip(", ")

        table.update_item(
            Key={'studentId': student_id},
            UpdateExpression=update_expression,
            ExpressionAttributeValues=expression_values
        )

        return {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "PUT,OPTIONS"
            },
            "body": json.dumps({"message": "Student updated successfully"})
        }

    except Exception as e:
        return {"statusCode": 500, "body": json.dumps({"error": str(e)})}
