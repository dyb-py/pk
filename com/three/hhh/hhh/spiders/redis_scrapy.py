# -*- coding: utf-8 -*-
import scrapy


class RedisScrapySpider(scrapy.Spider):
    name = 'redis-scrapy'
    allowed_domains = ['aaa']
    start_urls = ['http://aaa/']

    def parse(self, response):
        pass
