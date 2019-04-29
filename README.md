# Youdao-translate
Web Interface of Youdao AI Translation

* tanslate.py 可以本地执行，也可直接作为cgi程序。调用PC版web接口。
* update_passcode.py 更新passcode，写入passcode.txt，供translate.py调用（目测有道几天就会更新一次）。如果passcode过期，仍可翻译，但不会掉用AI接口。
* translate_mobile.py 只能本地执行。调用移动版web接口，接口虽简单，但对字数有限制，所以用它。
