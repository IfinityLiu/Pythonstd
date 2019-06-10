# -*- coding: utf-8 -*-
# 目标文件

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FirstItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    content = scrapy.Field()  # 创建容器
    link = scrapy.Field()  # 创建一个存储链接

# class QsbkItem
