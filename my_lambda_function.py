import json

def lambda_handler(event, context):
  print('in lambda_handler')
  print(event)
  http_method = event['httpMethod']
  query_parameters = event['queryStringParameters']
  print(http_method, query_parameters)
  response = {
    "statusCode":200,
    "body":json.dumps({
      "message":"hello python lambda",
      "httpMethod":http_method,
      "query_parameters":query_parameters
      })
  }

  return response