import requests
from lxml import etree
header = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"}
# 调度器（深度优先类）
class DFS():
    # 属性
    def __init__(self):
        # 容器：存放未爬过的url
        self.dfs = []
        # 容器：存放已爬过的url
        self.crawled = []
    # 方法
    # 存
    def save_url(self,url):
        if url not in self.crawled:  # 未爬过的url扔进去
            self.dfs.append(url)
    # 取
    def get_url(self):
        url = self.dfs.pop() # 取出url
        self.crawled.append(url) # 取出来的url放进已爬取的
        return url
class Crawl():
    def __init__(self):
        self.dfs = DFS()  # 组合
    def crawl(self):
        url = "http://www.baidu.com"
        self.dfs.save_url(url)  # 把首页的url扔进未爬取的容器中
        while True:
            try:
                new_url = self.dfs.get_url()
                res = requests.get(new_url,headers=header,timeout=3)
                ele = etree.HTML(res.content.decode())
                urls = ele.xpath("//a/@href") # 当前页所有的url组成的列表
                name = ele.xpath("//title/text()")[0]
                for url in urls:
                    if self.check_url(url):
                        print(url)
                        self.dfs.save_url(url)
            except:
                pass
    def check_url(self,url):
        if url.startswith("http://") or url.startswith("https://"):
            return True
        return False
if __name__ == '__main__':
    crawl = Crawl()
    crawl.crawl()


