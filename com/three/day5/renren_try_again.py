import requests
from lxml import etree
from chaojiying import get_code
url = "http://www.renren.com/228113725/profile"
cookies = {
    "t":"6c6ac64833374a0f316580451261744f7"
}
for i in range(110):
    res = requests.get(url,cookies=cookies).text
    ele = etree.HTML(res)
    # persons = ele.xpath("//div[@id='footprint-box']/ul/li/a/@href")
    name = ele.xpath("//title/text()")
    print(name[0])
    if name[0]=="人人网 - 验证码":
        image_url = ele.xpath("//div[@class='optional']/img/@src")[0]  # 获取图片
        im = requests.get(image_url,cookies=cookies).content  # 拿到图片的二进制流
        with open("1.jpg","wb") as w:
            w.write(im)
        code = get_code(im).get("pic_str")
        data = {
            'id': '880792860',
            'icode': code,
            'submit': '继续浏览',
            'requestToken': '-1330999392',
            '_rtk': '7c6b8dfa',
        }
        requests.post("http://www.renren.com/validateuser.do",data=data,cookies=cookies)
