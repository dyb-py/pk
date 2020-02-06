# -*- coding: utf-8 -*-
import scrapy
from ..items import Job51Item

class Job511Spider(scrapy.Spider):
    name = 'job511'

    def start_requests(self):
        pagenum = 1
        while True:
            url = 'https://search.51job.com/list/010000,000000,0000,00,9,99,java,2,'+str(pagenum)+'.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
            pagenum += 1
            yield scrapy.Request(url=url)

    def parse(self, response):
        item = Job51Item()
        title = response.xpath("//p[@class='t1 ']//a/text()")
        for i in title:
            item['title']=i.extract().strip()
            yield item