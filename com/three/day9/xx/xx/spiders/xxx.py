# -*- coding: utf-8 -*-
import scrapy


class XxxSpider(scrapy.Spider):
    name = 'xxx'
    allowed_domains = ['xxxxxx.com']
    start_urls = ['http://xxxxxx.com/']

    def parse(self, response):
        pass
