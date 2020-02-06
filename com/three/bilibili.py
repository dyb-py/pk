import requests
def down(url,name):
    video = requests.get(url,headers=header).content
    with open(name+'.mp4','wb') as r:
        r.write(video)
url = 'https://api.vc.bilibili.com/board/v1/ranking/top?page_size=10&next_offset=&tag=%E4%BB%8A%E6%97%A5%E7%83%AD%E9%97%A8&platform=pc'
header = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}
data = {
'page_size': '10',
'next_offset': '',
'tag': '今日热门',
'platform': 'pc'
}
res = requests.get(url,params=data).json()

for i in res['data']['items']:
    down(i['item']['video_playurl'],i['item']['description'])
    print(i['item']['video_playurl'])