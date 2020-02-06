# -*- coding: utf-8 -*-
import scrapy
import json
from ..items import BaiduItem
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}

class BaiduimgSpider(scrapy.Spider):
    name = 'baiduimg'
    # allowed_domains = ['baidu.com']
    # start_urls = ['http://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E9%AB%98%E6%B8%85%E5%8A%A8%E6%BC%AB&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&hd=&latest=&copyright=&word=%E9%AB%98%E6%B8%85%E5%8A%A8%E6%BC%AB&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&expermode=&force=&pn=60&rn=30&gsm=&1578301938325=']
    def start_requests(self):
        page = 0
        while True:
            url='http://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E9%AB%98%E6%B8%85%E5%8A%A8%E6%BC%AB&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&hd=&latest=&copyright=&word=%E9%AB%98%E6%B8%85%E5%8A%A8%E6%BC%AB&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&expermode=&force=&pn='+str(page)+'&rn=30&gsm=&1578301938325='
            page+=30
            yield scrapy.Request(url=url,headers=headers)

    def parse(self, response):
        item = BaiduItem()
        res = json.loads(response.text)
        for i in res['data']:
            item['url']=i["hoverURL"]
            yield item
