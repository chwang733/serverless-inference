import json
import base64
from botocore.vendored import requests

def lmInference(event, context):

    r=requests.get("http://chihchungwang.synology.me:8082/lm/inference")

    response = {
        "statusCode": 200,
        "headers": {"Access-Control-Allow-Origin": "*"},
        "body": r.text
    }

    return response

def icInference(event, context):

    #load test image - encode/decode for testing purpose
    image_read = open('00000001.jpg', 'rb').read() 
    image_64_encode = base64.encodestring(image_read)
    img=base64.decodestring(image_64_encode)

    #image_64_encode = event['body']
    
    files = {'file': ('00000002.jpg', img, 'multipart/form-data', {'Expires': '0'})}

    r= requests.post('http://chihchungwang.synology.me:8082/bears/inference', files=files)
    retJ=r.json()
    print(retJ["response"]["label"])
    

    response = {
        "statusCode": 200,
        "headers": {"Access-Control-Allow-Origin": "*"},
        "body": r.text
    }


    return response


