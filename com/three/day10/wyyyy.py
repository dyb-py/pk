import requests

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
    'referer': 'https://music.163.com/song?id=561493928',
}

url = ''

res = requests.get(url=url,headers=headers)
print(res.text)