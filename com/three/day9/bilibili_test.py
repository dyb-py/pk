import requests
import random
import time
def get_json(url):
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
    }

    params = {
        'page_size': 10,
        'next_offset': str(num),
        'tag': '今日热门',
        'platform': 'pc'
    }

    try:
        html = requests.get(url,params=params,headers=headers)
        return html.json()

    except BaseException:
        print('request error')
        pass

def download(url, path):
    start = time.time()  # 开始时间
    size = 0
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
    }
    # 默认情况下，发起请求会同时下载响应头和响应体（就是响应内容）
    # 如果将stream=True 则会推迟响应内容的下载
    response = requests.get(url, headers=headers, stream=True)
    chunk_size = 1024
    content_size = int(response.headers['content-length'])
    if response.status_code == 200:
        print('[文件大小]:%0.2f MB' % (content_size / chunk_size / 1024))
        #获取请求的原始响应可以用：Response.raw、Response.iter_content
        #普通情况可以用 r.raw，在初始请求中设置 stream=True,来获取服务器的原始套接字响应
        #当流下载时，用Response.iter_content或许更方便些。requests.get(url)默认是下载在内存中的，下载完成才存到硬盘上，可以用Response.iter_content　来边下载边存硬盘
        with open(path, 'wb') as file:
            for data in response.iter_content(chunk_size=chunk_size): #
                file.write(data)
                size += len(data)


if __name__ == '__main__':
    for i in range(10):
        url = 'http://api.vc.bilibili.com/board/v1/ranking/top?'
        num = i * 10 + 1
        html = get_json(url)
        infos = html['data']['items']
        for info in infos:
            title = info['item']['description']  # 小视频的标题
            video_url = info['item']['video_playurl']  # 小视频的下载链接
            print(title)

            # 为了防止有些视频没有提供下载链接的情况
            try:
                download(video_url, path='%s.mp4' % title)
                print('成功下载一个!')


            except BaseException:
                print('凉凉,下载失败')
                pass

        time.sleep(int(format(random.randint(2, 8))))