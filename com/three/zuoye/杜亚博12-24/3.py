from urllib import request

url='https://maoyan.com/board/4'

res=request.urlopen(url)
print(res.read().decode())