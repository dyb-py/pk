import wordcloud
import numpy as np
from PIL.Image import open as o

with open('wyyyy.txt','r',encoding='utf-8') as r:
    s = r.read()
# with open('xufulin.png','rb') as r:
#     n = r.read()
n = np.array(o(r'E:\Python186共享文件夹\第三阶段\代码\day10\xufulin.jpg'))
w = wordcloud.WordCloud(font_path=r'E:\Python186共享文件夹\第三阶段\代码\day10\simhei.ttf',mask=n)
w.generate(s)
w.to_file('wyyyy.jpg')