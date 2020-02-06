# -*- coding: utf-8 -*-
import scrapy
from ..items import MaoyanTestItem

class MyTestSpider(scrapy.Spider):
    name = 'my_test'
    allowed_domains = ['baidu.com']

    headers = {
        'hexin':'woman'
    }

    cookies = {
        'hexin':'TheShuai'
    }

    data = {
        'name':'hexin',
        'pass':'666666',
    }
    def start_requests(self):
        url='https://www.httpbin.org/cookies'
        import json
        # data = str(self.data)
        #如果你的allowed_domains过滤你的url，可以设置dont_filter不过滤
        yield scrapy.Request(url=url,cookies=self.cookies,dont_filter=True)
        # yield scrapy.FormRequest(url=url,formdata=self.data)

    def parse(self, response):
        print(response.text)