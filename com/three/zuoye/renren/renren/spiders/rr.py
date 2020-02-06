# -*- coding: utf-8 -*-
import scrapy
from ..items import RenrenItem
cookies={
't':'99fe0d042050a0faabd7cac04e2951e70'
}
class RrSpider(scrapy.Spider):
    name = 'rr'
    def start_requests(self):
        url='http://www.renren.com/880151247/profile'
        yield scrapy.Request(url=url,cookies=cookies)
    def parse(self, response):
        item = RenrenItem()
        res = response.xpath("//div[@id='footprint-box']/ul/li/a/@namecard")
        for i in res:
            # print(i.extract())
            url = 'http://www.renren.com/'+i.extract()+'/profile'
            item['id']=i.extract()
            yield item
            yield scrapy.Request(url=url,cookies=cookies,callback=self.parse)
