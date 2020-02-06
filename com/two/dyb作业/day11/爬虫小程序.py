# 百度
# from urllib import request
# # 定义一个url
# url = "http://www.baidu.com"
# # 发送请求并返回一个响应结果
# response = request.urlopen(url)
# # 使用read方法获取相应的内容，并对其进行解码
# html = response.read().decode()
# # 保存内容
# with open("baidu.html","w",encoding="utf-8") as f:
#     f.write(html)
from urllib import request
import re
import MySQLdb
url = "http://www.521609.com"   # 定义url

# 获取网页
def get_html(url):
    return request.urlopen(url).read().decode("gb2312")   # 返回html字符串

# 获取图片路由
def get_url(html):
    rule = "src='(.*?).jpg'"   # 写规则
    img_compile = re.compile(rule)  # 编译
    img_url = img_compile.findall(html)  # 匹配
    return img_url

# 保存进本地
# def save(img_url):
#     num = 0
#     for imgs in img_url:
#         new_img_url = url+imgs+".jpg"
#         request.urlretrieve(new_img_url,str(num)+".jpg")
#         num += 1

# 地址保存进数据库
def save(img_url):
    # 连接数据库
    conn = MySQLdb.connect(host="localhost",port=3306,user="root",password="123456",db="userdb",charset="utf8")
    cursor = conn.cursor()  # 获取游标
    for imgs in img_url:
        # 获取图片url
        new_img_url = url + imgs + ".jpg"
        # 定义sql语句
        sql = "insert into imgurl(urlname)values(%s)"
        # 执行sql语句
        cursor.execute(sql,(new_img_url,))
        # 提交事务
        conn.commit()
#  调用函数
html = get_html(url)
img_url = get_url(html)
save(img_url)







