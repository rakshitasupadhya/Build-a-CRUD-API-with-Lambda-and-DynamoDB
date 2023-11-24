import boto3
import json

dynamodb = boto3.resource('dynamodb')
tableName = "CRUD-DB"
table = dynamodb.Table(tableName)

def lambda_handler(event, context):
    print('Line11', event)
    body = None
    statusCode = 200
    headers = {
        "Content-Type": "application/json",
    }
    try:
        if event['routeKey'] == "DELETE /items/{ID}":
            id= event['queryStringParameters']['ID']
            response= table.delete_item(
                Key={
                    "ID": id
                }
            )
            body = f"Deleted item {event['queryStringParameters']['ID']}"

        elif event["routeKey"] == "GET /items/{ID}":
            id= event['queryStringParameters']['ID']
            response = table.get_item(
                Key={
                    "ID": id
                }
            ).get('Item')
            body = response
            
        elif event["routeKey"] == "GET /items":
            response = table.scan(
            )
            body = response.get("Items", [])
            
        elif event['routeKey'] == "PUT /items":
            requestJSON = json.dumps(event['queryStringParameters'])
            request_data_str = json.loads(requestJSON)
            table.put_item(
                
                Item=request_data_str
            )
            body =f"Item added successfully {event['queryStringParameters']['ID']}"

    except Exception as e:
        statusCode = 500
        body = str(e)

    return {
        "statusCode": statusCode,
        "headers": headers,
        "body": json.dumps(body)
    }



