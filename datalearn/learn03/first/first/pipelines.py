# -*- coding: utf-8 -*-
# 后续处理文件

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class FirstPipeline(object):
    def process_item(self, item, spider):
        # 通过for循环处理链接
        for i in range(0, len(item['content'])):
            print(item['content'][i])
            print(item['link'][i])

        return item
