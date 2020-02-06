# -*- coding: utf-8 -*-
import scrapy

class ScrapyResponseSpider(scrapy.Spider):
    name = 'scrapy_response'
    # allowed_domains = ['xxx.com']
    # start_urls = ['http://xxx.com/']
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
            }

    def start_requests(self):
        url = 'https://www.zhipin.com/job_detail/?query=python&city=101010100&industry=&position='
        yield scrapy.Request(url=url,headers=self.headers)

    def parse(self, response):
        print(response.text)
        print(response.headers)
