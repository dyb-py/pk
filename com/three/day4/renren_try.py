# import requests
# from lxml import etree
# url = "http://www.renren.com/880151247/profile"
# for i in range(110):
#     res = requests.get(url,cookies={"t":"8ff66ae8cc11bdb9d5a5e26133a8e2a82"}).text
#     ele = etree.HTML(res)
#     # persons = ele.xpath("//div[@id='footprint-box']/ul/li/a/@href")
#     name = ele.xpath("//title/text()")
#     print(name[0])
from PIL import Image
import pytesseract
text=pytesseract.image_to_string(Image.open('0.jpg'),lang='chi_sim')
print(text)
