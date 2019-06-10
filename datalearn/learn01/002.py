# -*- coding:utf-8 -*-
# Author: Aaron


import urllib.request
import urllib.parse
import string


def get_method_params():
    url = "http://www.baidu.com/s?wd="
    # 拼接字符串
    name = '美女'
    final_url = url + name
    print(final_url)
    # 不转义就会报错，需要将中文进行转义,将包含汉字的网址进行转义
    encode_new_url = urllib.parse.quote(final_url, safe=string.printable)
    print(encode_new_url)
    # 使用代码发送网络请求
    response = urllib.request.urlopen(encode_new_url)
    print(response)
    # 读取内容
    data = response.read().decode()
    print(data)
    # 保存
    with open("02-encode.html", 'w', encoding='utf-8')as f:
        f.write(data)


get_method_params()
