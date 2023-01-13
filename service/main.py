import json

def lambda_handler(event: dict, context: dict):
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({"message": "hello world!"})
    }