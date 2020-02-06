# -*- coding: utf-8 -*-
import scrapy


class ScrapyPostSpider(scrapy.Spider):
    name = 'scrapy_post'
    data = {
        'name':'123',
        'pass':'123'
    }

    def start_requests(self):
        url = 'https://www.iqianyue.com/mypost'
        yield scrapy.FormRequest(url=url,formdata=self.data)

    def parse(self, response):
        print(response.text)
