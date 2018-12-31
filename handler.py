import json

from urllib.request import urlopen

def lmInference(event, context):
    
#    body = { "response" : {
#        "text": "Hello Serverless v1.0! Your function executed successfully!"
#        }
#    }


 
    ret = urlopen("http://chihchungwang.synology.me:8082/lm/inference")
    body = json.load(ret)

    response = {
        "statusCode": 200,
        "headers": {"Access-Control-Allow-Origin": "*"},
        "body": json.dumps(body)
    }

    return response

def bye(event, context):
    body = {
        "message": "Bye Serverless ! Your function executed successfully!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response


    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
