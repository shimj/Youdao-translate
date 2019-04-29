#!/usr/bin/env python3
import requests
import json
import js2py
import hashlib

url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

context = js2py.EvalJs()
js_str = """r = "" + (new Date).getTime()
          , i = r + parseInt(10 * Math.random(), 10);"""
context.execute(js_str)
ts = context.r
salt = context.i

headers = {
    'Pragma': "no-cache",
    'Origin': "http://fanyi.youdao.com",
    'Accept-Encoding': "gzip, deflate",
    'Accept-Language': "en-US",
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.2 Safari/605.1.15",
    'Content-Type': "application/x-www-form-urlencoded; charset=UTF-8",
    "Content-Length": "255",
    'Accept': "application/json, text/javascript, */*; q=0.01",
    'Cache-Control': "no-cache",
    'X-Requested-With': "XMLHttpRequest",
    'Connection': "keep-alive",
    'Referer': "http://fanyi.youdao.com/",
    # have not figured out the first cookie value, so just deleted
    #'Cookie': '___rl__test__cookies='+str(int(ts)-200)+'; JSESSIONID=aaaDnt9cbBF1ng4Z7LIPw; OUTFOX_SEARCH_USER_ID=-1433964397@10.169.0.84; OUTFOX_SEARCH_USER_ID_NCOO=1589531276.57051'
    'Cookie': 'JSESSIONID=aaaDnt9cbBF1ng4Z7LIPw; OUTFOX_SEARCH_USER_ID=-1433964397@10.169.0.84; OUTFOX_SEARCH_USER_ID_NCOO=1589531276.57051'
}

e = "Bloody limbs lay about"
passcode = "p09@Bn{h02_BIEe]$P^nG"
passcode = "@6f#X3=cCuncYssPsuRUE"
with open("./passcode.txt") as f:
    passcode = f.read()
sign = hashlib.md5(("fanyideskweb" + e + salt + passcode).encode('utf-8')).hexdigest()

data = {
    'i': e,
    'from': 'AUTO',
    'to': 'AUTO',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'salt': salt,
    'sign': sign,
    'ts': ts,
    'bv': 'd26c1cc70023e993de6ae8831dd44989',
    'doctype': 'json',
    'version': '2.1',
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_REALTlME'
}

resp = requests.post(url=url, headers=headers, data=data)
resp_dict = json.loads(resp.text)
ret = resp_dict['translateResult'][0][0]['tgt']
print(ret)
