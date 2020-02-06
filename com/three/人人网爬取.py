import requests
from lxml import etree
from chaojiying import get_code
import MySQLdb
conn = MySQLdb.connect(
    db="spider",
    user="root",
    passwd="123456",
    host="localhost",
    port=3306,
    charset='utf8'
)
cursor = conn.cursor()
url = "http://www.renren.com/228113725/profile"
cookies = {
    "t":"d9b00f38123103075a85551d3e7f7bd92"
}
# 发送获取到的url
def send_url(url):
    res = requests.get("http://www.renren.com/"+url+"/profile",cookies=cookies).text
    ele = etree.HTML(res)
    try:
        name = ele.xpath("//title/text()")[0]
        print(name)
        if name == "人人网 - 验证码":
            check_code(ele)  # 破解验证码
        save_data(name)
        urls = ele.xpath("//div[@id='footprint-box']/ul/li/a/@namecard")
        for url in urls:
            try:
                save_url(url)
            except:
                pass
    except:
        pass
# 检测获取到验证码
def check_code(ele):
    image_url = ele.xpath("//div[@class='optional']/img/@src")[0]  # 获取图片
    im = requests.get(image_url, cookies=cookies).content  # 拿到图片的二进制流
    with open("1.jpg", "wb") as w:
        w.write(im)
    code = get_code(im).get("pic_str")
    data = {
        'id': '880792860',
        'icode': code,
        'submit': '继续浏览',
        'requestToken': '-1330999392',
        '_rtk': '7c6b8dfa',
    }
    requests.post("http://www.renren.com/validateuser.do", data=data, cookies=cookies)
# 保存数据
def save_data(name):
    sql = "insert into renren_data values (%s)"
    cursor.execute(sql,[name])
# 保存抓取下来的url
def save_url(url):
    sql = "insert into renren_url values(%s,%s)"
    cursor.execute(sql,(url,"0"))
    conn.commit()
# 从数据库中取值
def get_url():
    sql = "select url from renren_url where flag=%s"  # 从数据库中取出一个状态为0的url
    cursor.execute(sql,['0'])
    url = cursor.fetchone()[0]
    sql = "update renren_url set flag=%s where url=%s"  # 设置取出来的url状态为1
    cursor.execute(sql,['1',url])
    send_url(url)
    conn.commit()
if __name__ == '__main__':
    while True: # 循环获取url
        get_url()









