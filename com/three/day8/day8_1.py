import requests
url = 'http://www.httpbin.org/headers'


res = requests.get(url=url)
print(res.text)