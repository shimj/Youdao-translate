#!/usr/bin/env python3
import requests
import json
import time
import random
import hashlib

import sys
import codecs
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

def get_ts():
    ts = str(int(1000 * time.time()))
    return ts

def get_salt(ts):
    salt = ts + str(random.randint(0, 10))
    return salt

def get_sign(query, salt):
    passcode = "p09@Bn{h02_BIEe]$P^nG"
    passcode = "@6f#X3=cCuncYssPsuRUE"
    with open("./passcode.txt") as f:
        passcode = f.read()
    content = 'fanyideskweb' + query + salt + passcode
    sign = hashlib.md5(content.encode('utf-8')).hexdigest()
    return sign

def translate(query, first_timeout=0.8):
    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

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

    ts = get_ts()
    salt = get_salt(ts)
    sign = get_sign(query, salt)
    data = {
        'i': query,
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

    try:
        resp = requests.post(url=url, headers=headers, data=data, timeout=first_timeout)
    except:
        resp = requests.post(url=url, headers=headers, data=data)
    resp_dict = json.loads(resp.text)
    ret = "\n".join(["".join([item["tgt"] for item in line]) for line in resp_dict['translateResult']])
    return ret

def get_cgi_data():
    import cgi
    form = cgi.FieldStorage()
    q = form.getvalue('q')
    return q

def to_html(text):
    html = "Content-Type:text/html\n\n<!DOCTYPE html>\n<html>\n<body>"+text.replace("\n", "<br>")+"</body>\n</html>"
    return html

if __name__ == '__main__':
    query = get_cgi_data()
    if not query:
        if len(sys.argv)>1:
            query = sys.argv[1]
        else:
            query = "Bloody limbs lay about" #血淋淋的四肢横七遍野
        result = translate(query)
        print(result)
    else:
        result = translate(query)
        html = to_html(result)
        print(html)
