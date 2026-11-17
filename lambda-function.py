
import json

def lambda_handler(event, context):

    method = event.get("requestContext", {}).get(
        "http", {}
    ).get("method", "GET")

    # GET request
    if method == "GET":

        response_data = {
            "message": "Welcome to AWS Serverless API!",
            "status": "Success",
            "technology": "AWS Lambda",
            "method": "GET"
        }

        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": json.dumps(response_data)
        }

    # POST request
    elif method == "POST":

        body = event.get("body", "{}")

        if isinstance(body, str):
            body = json.loads(body)

        name = body.get("name", "User")

        response_data = {
            "message": f"Hello {name}!",
            "status": "Success",
            "method": "POST"
        }

        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": json.dumps(response_data)
        }

    # Unsupported method
    else:
        return {
            "statusCode": 405,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": json.dumps({
                "message": "Method not allowed"
            })
        }
