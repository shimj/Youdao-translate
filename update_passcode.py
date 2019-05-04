#!/usr/local/bin/python3
import requests
import re
import os, inspect
current_file_path = os.path.abspath(inspect.getfile(inspect.currentframe()))
base_path = os.path.dirname(current_file_path)
os.chdir(base_path)

url = "http://shared.ydstatic.com/fanyi/newweb/v1.0.17/scripts/newweb/fanyi.min.js"
headers = {
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.2 Safari/605.1.15",
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-us',
    'Upgrade-Insecure-Requests': '1',
    'X-Requested-With': "XMLHttpRequest",
    'Connection': "keep-alive",
    'Referer': "http://fanyi.youdao.com/",
}


resp = requests.get(url=url)
js_data = resp.text
result = re.findall(r"sign:\s?n\.md5[^\)]+\"([^\"]*)\"\)", js_data)[0]
with open("./passcode.txt", "w") as f:
    f.write(result)
