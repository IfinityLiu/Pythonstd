# -*- coding:utf-8 -*-
# Author: Aaron


import urllib.request
import urllib.parse
import string


def get_params():
    url = "http://www.baidu.com/s?wd="
    params = {
        "wd": "美女",
        "key": "zhang",
        "value": "san"
    }
    str_params = urllib.parse.urlencode(params)
    print(str_params)
    final_url = url + str_params

    # 将带有中文的url转义
    end_url = urllib.parse.quote(final_url, safe=string.printable)

    response = urllib.request.urlopen(end_url)
    
    data = response.read().decode("utf-8")
    print(data)


get_params()
