# -*- coding: utf-8 -*-
import scrapy

from first.items import FirstItem
from scrapy.http import Request


class QsbkSpider(scrapy.Spider):
    name = 'qsbk'
    allowed_domains = ['qiushibaike.com']
    '''
    start_urls = ['http://qiushibaike.com/hot/']
    '''

    def start_requests(self):
        ua = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
        yield Request('http://qiushibaike.com/hot/', headers=ua)

    def parse(self, response):
        it = FirstItem()
        it['content'] = response.xpath(
            "//div[@class='content']/span/text()").extract()
        it['link'] = response.xpath(
            "//a[@class='contentHer']/@href").extract()
        yield it
