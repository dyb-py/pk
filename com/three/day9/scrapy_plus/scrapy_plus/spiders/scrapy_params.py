# -*- coding: utf-8 -*-
import scrapy


class ScrapyParamsSpider(scrapy.Spider):
    name = 'scrapy_params'
    # allowed_domains = ['xxx.com']
    # start_urls = ['http://xxx.com/']


    def start_requests(self):
        url = 'http://www.httpbin.org/headers?hexin=man'
        yield scrapy.Request(url=url)

    def parse(self, response):
        print(response.body)
