#!/usr/local/bin/python3
import sys
import os, inspect
current_file_path = os.path.abspath(inspect.getfile(inspect.currentframe()))
base_path = os.path.dirname(current_file_path)
os.chdir(base_path)
sys.path.append("../BTT_WebView/popup_template")
from popup import update
from translate import translate
import subprocess

def beautify(origin, translation):
    return ''.join(['<div style="font-size: 18px">', translation,
        '</div><br><br><div style="font-size: 18px;color: grey">', "原文：", origin, '</div>'])

if __name__ == '__main__':
    if len(sys.argv)>1:
        text = sys.argv[1]
    else:
        text = subprocess.getoutput("pbpaste")
    update(beautify(text, translate(text)))