# -*- coding: utf-8 -*-
import scrapy


class ScrapyHeadersSpider(scrapy.Spider):
    name = 'scrapy_headers'
    # allowed_domains = ['xxx.com']
    # start_urls = ['http://xxx.com/']
    headers = {
        'minghan':'cuishen'
    }

    def start_requests(self):
        url = 'http://www.httpbin.org/headers'
        yield scrapy.Request(url=url,headers=self.headers)


    def parse(self, response):
        print(response.text)
