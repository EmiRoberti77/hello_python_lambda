from my_lambda_function import lambda_handler

event = {
  "httpMethod": "GET",
    "path": "/resource",
    "queryStringParameters": {
        "param1": "value1",
        "param2": "value2"
    },
    "headers": {
        "Host": "example.com",
        "User-Agent": "Postman"
    },
    "body": None,  
    "isBase64Encoded": False
}

response = lambda_handler(event, None)
print(response)