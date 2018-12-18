# -*- coding: utf-8 -*-
# flake8: noqa
import requests
from qiniu import Auth
 
 
access_key = '填写AK'
secret_key = '填写SK'
q = Auth(access_key, secret_key)
url = 'http://api.qiniu.com/pfop/'

body = 'bucket=bucket名&key=index.txt&fops=mkzip%2f4%7csaveas%2fcWRvd250czpzZXZlbjAxLnppcA%3d%3d' #填写对应参数
#格式参考文档 https://developer.qiniu.com/dora/manual/1667/mkzip#2
 
qbox_token= 'QBox '+ q.token_of_request(url,body=body,content_type="application/x-www-form-urlencoded")
 
 
r = requests.post(url, data=body, headers={'Authorization': qbox_token, 'Content-Type': 'application/x-www-form-urlencoded'})
print(r)
print(r.text)
