from urllib import request
import json
pagenum = 0
num = 0
while True:
    url = "https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E6%96%97%E5%9B%BE&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=&hd=&latest=&copyright=&word=%E6%96%97%E5%9B%BE&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&expermode=&force=&pn="+str(pagenum)+"&rn=30"
    pagenum += 30
    res = json.loads(request.urlopen(url).read().decode())
    for i in res['data']:
        try:
            print(i["hoverURL"])
            request.urlretrieve(i["hoverURL"],"E:\\Python186共享文件夹\\第三阶段\\代码\\day2\\image\\"+str(num)+".jpg")
            num += 1
        except:
            pass
