from urllib import request as req
from lxml import etree
num = 0
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"}
while num < 100:
    url = "https://maoyan.com/board/4?offset="+str(num)
    num += 10
    request = req.Request(url,headers=headers)
    res = req.urlopen(request).read().decode()
    ele = etree.HTML(res)
    movie_urls = ele.xpath("//p[@class='name']/a/@href")
    for movie_url in movie_urls:
        request = req.Request("https://maoyan.com"+movie_url, headers=headers)
        res = req.urlopen(request).read().decode()
        ele = etree.HTML(res)
        movie_name = ele.xpath("//h3[@class='name']/text()")
        print(movie_name)

