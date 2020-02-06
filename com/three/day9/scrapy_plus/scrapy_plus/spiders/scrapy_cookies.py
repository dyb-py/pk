# -*- coding: utf-8 -*-
import scrapy


class ScrapyCookiesSpider(scrapy.Spider):
    name = 'scrapy_cookies'
    # allowed_domains = ['xxx.com']
    # start_urls = ['http://xxx.com/']
    cookies={
        'liuminghan':'like rolling in the louti'
    }

    def start_requests(self):
        url = 'http://www.httpbin.org/cookies'
        yield scrapy.Request(url=url,cookies=self.cookies)


    def parse(self, response):
        print(response.text)
