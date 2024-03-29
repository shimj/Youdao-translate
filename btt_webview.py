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
    return ''.join(['<div id="translation" style="font-size: 18px">', translation,
        '</div><br><br><div style="font-size: 18px;color: grey">', "原文：", origin, '</div>'])

if __name__ == '__main__':
    if len(sys.argv)>1:
        text = sys.argv[1]
    else:
        text = subprocess.getoutput("pbpaste")
    translate_result = translate(text)

    passcode_update_code_path = os.path.join(base_path, "update_passcode.py")
    js_code = '''function update_passcode() {
            $("#update_passcode").css("pointer-events","none");
            exec_shell("'''+passcode_update_code_path+'''",
                ()=>window.BTT.callHandler('execute_assigned_actions_for_trigger', {closeFloatingHTMLMenu: 1}));
            }
            document.addEventListener('keydown', (event) => {
                const keyCode = event.keyCode;
                if (keyCode === 67) {
                    copyToClipboard($("#translation").text())
                }
            }, false);'''
    update(beautify(text, translate_result)+'''<br><br><div id=\"update_passcode\" style=\"text-align:right\">
        <a href=\"javascript:update_passcode();\">Update Passcode</a></div>''', "", js_code)