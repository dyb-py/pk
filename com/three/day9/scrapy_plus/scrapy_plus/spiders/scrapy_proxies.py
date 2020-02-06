# -*- coding: utf-8 -*-
import scrapy


class ScrapyProxiesSpider(scrapy.Spider):
    name = 'scrapy_proxies'
    # allowed_domains = ['xxx.com']
    # start_urls = ['http://xxx.com/']
    meta = {}
    meta['proxy']='http://119.147.137.79:8008'

    def start_requests(self):
        url = 'http://www.httpbin.org/ip'
        yield scrapy.Request(url=url)

    def parse(self, response):
        print(response.text)
