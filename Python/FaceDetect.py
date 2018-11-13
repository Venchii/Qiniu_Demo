
"""
接口文档：https://developer.qiniu.com/dora/manual/4438/face-recognition
显示所有的人像库
"""
import requests
from qiniu import QiniuMacAuth

with open('key.txt','r') as f1:
    keys = f1.readlines()

access_key = keys[0].strip('\n')
secret_key = keys[1].strip('\n')


#生成鉴权QiniuToken
auth = QiniuMacAuth(access_key,secret_key)

url = "http://ai.qiniuapi.com/v1/face/group"
token = "Qiniu " + auth.token_of_request(method="GET",url = url)

headers = {
    "Authorization":token,
    "Host":"ai.qiniuapi.com"
}

response = requests.get(url,headers = headers)
print(response.status_code,response.text)
