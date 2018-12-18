# -*- coding: utf-8 -*-
# flake8: noqa
import requests
from qiniu import Auth
access_key = '填写ak'
secret_key = '填写sk'
q = Auth(access_key, secret_key)

url = 'http://rsf.qiniu.com/v2/list?bucket=bucket名&prefix=前缀名&limit=3'  #填写对应参数
#参数格式参考文档  https://developer.qiniu.com/kodo/api/1284/list

qbox_token = 'QBox '+ q.token_of_request(url,content_type="application/x-www-form-urlencoded")

r = requests.post(url, headers={'Authorization': qbox_token, 'Content-Type': 'application/x-www-form-urlencoded'})


print(r)
print(r.text)
