# -*- coding: utf-8 -*-
import scrapy
import time
from ..items import FirstScrapyProjItem

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}

class BiqugeSpider(scrapy.Spider):
    name = 'biquge'
    # start_urls = ['http://www.xbiquge.la/xiaoshuodaquan/']
    def start_requests(self):
        url = 'http://www.xbiquge.la/xiaoshuodaquan/'
        yield scrapy.Request(url=url)

    def parse(self, response):
        time.sleep(1)
        for i in response.xpath("//div[@id='main']/div/ul/li/a/@href"):
            url = i.extract()
            yield scrapy.Request(url=url,callback=self.parse2,headers=headers)

    def parse2(self,response):
        time.sleep(1)
        for j in response.xpath("//div[@id='list']//dd/a/@href"):
            url = 'http://www.xbiquge.la'+j.extract()
            yield scrapy.Request(url=url,callback=self.parse3,headers=headers)

    def parse3(self,response):
        zhangjie = response.xpath("//h1/text()")[0].extract()
        item = FirstScrapyProjItem()
        item['zhangjie'] = zhangjie
        yield item

