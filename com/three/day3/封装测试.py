from day3 import myurllib
from urllib import request
url = "http://www.xbiquge.la/xiaoshuodaquan/"
res = myurllib.get(url).xpath("//div[@class='novellist']//li/a/text()")
print(res)

