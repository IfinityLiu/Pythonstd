# -*- coding:utf-8 -*-
# Author: Aaron


import urllib.request


def load_data():
    url = 'http://www.baidu.com/'
    # response:http相应的对象
    response = urllib.request.urlopen(url)
    print(response)
    # 读取内容 bytes类型
    data = response.read()
    print(data)
    # 将文件获取的内容转换成字符串
    str_data = data.decode('utf-8')
    print(str_data)
    # 将数据写入文件
    with open('baidu.html', 'w', encoding='utf-8')as f:
        f.write(str_data)
    # 将字符串类型转换成bytes类型
    str_name = 'baidu'
    byte_name = str_name.encode('utf-8')
    print(byte_name)

    # python爬取的类型：str bytes
    # 如果爬取回来时bytes类型，但是你写入的时候需要字符串就使用 decode（'utf-8'）
    # 如果爬取回来时str类型，但是你写入的时候需要bytes就使用 encode（'utf-8'）


load_data()
