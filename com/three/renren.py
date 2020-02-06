import requests
from lxml import etree
import re
url = "http://www.renren.com/profile.do?portal=homeFootprint&ref=home_footprint&id=880151247"
rule="id=(.*)"
id_set={1}
def search(url):
    id=re.findall(rule, url)[0]
    if id in id_set:
        return 0
    id_set.add(id)
    res = requests.get(url, cookies={"t": "863feb942150e75dee878070bfefac980"}).text
    print(res)
    ele = etree.HTML(res)
    persons = ele.xpath("//div[@id='footprint-box']/ul/li/a/@href")
    name = ele.xpath("//*[@id='cover']/div[2]/h1/text()")
    xinxi = ele.xpath('//p[@class="authentication"]/text()')
    school = ele.xpath('//*[@id="operate_area"]/div[1]/ul/li[1]/span/text()')
    address = ele.xpath('//*[@id="operate_area"]/div[1]/ul/li[4]/text()')
    if not persons:
        return 0
    if name:
        print(name[0].strip())
    if xinxi:
        print(xinxi[0].strip())
    if school:
        print(school[0].strip())
    if address:
        print(address[0].strip())
    print('______________________')
    for pre in persons:
        search(pre)
search(url)