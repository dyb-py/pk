import jieba
import wordcloud




j = jieba.cut('无论如何遇到什么困难也不要怕,微笑着面对它,消除恐惧的最好办法就是面对恐惧,坚持才是胜利,加油,奥利给!')
s = ''
for i in j:
    s += i+','
print(s)

w = wordcloud.WordCloud(font_path=r'E:\Python186共享文件夹\第三阶段\代码\day10\simhei.ttf')
w.generate(s)
w.to_file('gun.jpg')




