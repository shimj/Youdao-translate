#!/usr/bin/env python3
import requests
import re
import sys

url = 'http://m.youdao.com/translate'
headers = {
    'Origin': "http://m.youdao.com",
    'Accept-Encoding': "gzip, deflate",
    'Accept-Language': "en-US",
    'User-Agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1 Mobile/15E148 Safari/604.1",
    'Content-Type': "application/x-www-form-urlencoded",
    'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    'X-Requested-With': "XMLHttpRequest",
    'Connection': "keep-alive",
    'Referer': "http://m.youdao.com/translate"#,
    #'Cookie': 'OUTFOX_SEARCH_USER_ID=2007723206@117.130.42.142'
}

if len(sys.argv)==1:
    e = "Bloody limbs lay about" #right result: 血淋淋的四肢横七遍野
else:
    e = sys.argv[1]

data = {"inputtext": e, "type": "AUTO"}

resp = requests.post(url=url, headers=headers, data=data)
result = re.findall(r"translateResult[\"\']>[\s\S]*?<li>([\s\S]*?)</li>", resp.text)[0]
print(result)