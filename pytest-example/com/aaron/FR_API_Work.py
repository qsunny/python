# -*- coding:utf-8 -*-
"""

pip install -U request
"""
__author__ = "aaron.qiu"

import base64
import hmac
import hashlib 
import binascii
from datetime import datetime
import requests
import json
from urllib import parse

# Getting the current date and time
dt = datetime.now()

# getting the timestamp
ts = datetime.timestamp(dt)
ts2 = int(ts)

header ='{"alg":"HS256","typ":"JWT"}'
payload = '{"user":"jamesshieh1111","timestamp":"' + str(ts2) + '"}'
#print(payload)
key = "hV4hJ1jF2fG4mB3jM1cD"
#convert utf-8 string to byte format
def toBytes(string):
    return bytes(string,'utf-8')

def encodeBase64(text):
    #remove "=" sign,
    #P.S. "=" sign is used only as a complement in the final process of encoding a message. 
    return base64.urlsafe_b64encode(text).replace(b'=',b'')

#signature = HMAC-SHA256(key, unsignedToken)
def create_sha256_signature(key, unsignedToken):
    signature = hmac.new(toBytes(key), unsignedToken, hashlib.sha256).digest()
    return encodeBase64(signature)

unsignedToken =encodeBase64(toBytes(header)) + toBytes('.') + encodeBase64(toBytes(payload))
signature =create_sha256_signature(key,unsignedToken)
jwt_token=unsignedToken.decode("utf-8") +'.'+signature.decode("utf-8")

url = "https://fr.scanvis-ai.com:8177/api/v1/face/compare/compare-url"
data2= {"source": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRNUJmENoAE4XcMmqqZ9eRA6LT-PvnzocT27A&usqp=CAU","target": "https://cdn4.premiumread.com/?url=https://malaymail.com/malaymail/uploads/images/2022/11/25/72014.jpeg&w=800&q=100&f=jpg&t=2"};
headers = {'Authorization': jwt_token, "Content-Type":"application/json"};
print("Send Request:" + datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])
r = requests.post(url,json=data2,headers=headers);
print("Response:" + datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])
print (r.content);
