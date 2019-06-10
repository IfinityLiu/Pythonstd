# -*- coding:utf-8 -*-
# Author: Aaron


from scrapy.spiders import Spider


class FirstSpider(Spider):
    name = 'first'  # 设置爬虫的名字
    allowed_domains = ['baidu.com']  # 控制允许爬取的域名
    start_urls = ['http://www.baidu.com']  # 起始URL

    def parse(self, response):  # 回调函数
        pass
