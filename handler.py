import json
import base64
from botocore.vendored import requests

from io import BytesIO
import json
from requests_toolbelt.multipart import MultipartDecoder

def test(event, context):

    content_type = event['headers']['content-type']
    post_data= base64.b64decode(event['body'])
    decoder=MultipartDecoder(post_data, content_type)
#    for part in decoder.parts:
#      print(part.content)

    
    files = {'file': ('00000002.jpg', decoder.parts[0].content, 'multipart/form-data', {'Expires': '0'})}

    r= requests.post('http://chihchungwang.synology.me:8082/bears/inference', files=files)
    retJ=r.json()
    print(retJ["response"]["label"])
    

    response = {
        "statusCode": 200,
        "headers": {"Access-Control-Allow-Origin": "*"},
        "body": r.text
    }


    return response


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
    #image_read = open('00000001.jpg', 'rb').read() 
    #image_64_encode = base64.encodestring(image_read)
    #img=base64.decodestring(image_64_encode)

    #Pase multipart/form-data to get the image binary
    content_type = event['headers']['content-type']
    post_data= base64.b64decode(event['body'])
    decoder=MultipartDecoder(post_data, content_type)
    img=decoder.parts[0].content

    files = {'file': ('sample.jpg', img, 'multipart/form-data', {'Expires': '0'})}

    r= requests.post('http://chihchungwang.synology.me:8082/bears/inference', files=files)
    retJ=r.json()
    print(retJ["response"]["label"])
    

    response = {
        "statusCode": 200,
        "headers": {"Access-Control-Allow-Origin": "*"},
        "body": r.text
    }


    return response


