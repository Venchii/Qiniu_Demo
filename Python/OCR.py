import requests
import json
from qiniu import QiniuMacAuth

access_key = '3gFTmZm'
secret_key = 'aF3_h9AwDE'


#生成鉴权QiniuToken
auth = QiniuMacAuth(access_key,secret_key)
body = json.dumps(
{
    "data": {
        "uri": "http://"
    }
}

)

url = "http://ai.qiniuapi.com/v1/ocr/idcard"
token = "Qiniu " + auth.token_of_request(method="POST",url = url,body=body,content_type="application/json")

header = {
    "Authorization":token,
    "Host":"ai.qiniuapi.com",
    "Content-Type":"application/json"
}

response = requests.post(url,headers = header,data=body)
print(response.status_code,response.text)
