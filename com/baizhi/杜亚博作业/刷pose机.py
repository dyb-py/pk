import threading
import random
import time

familyName=['赵','钱','孙','欧阳','上官','司马','慕容','诸葛','轩辕','令狐','宇文','李'] # 姓
firstName=['云','万','子','竹','婉','言','复','瑾','馥','哲','月','溪','秋','小','剑','沐']
middleName=['国','波','杰','儿','刚','雅','浩','飞','冲','姬','坤']

def getName():
    x=familyName[random.randint(0,len(familyName)-1)]
    z=firstName[random.randint(0,len(firstName)-1)]
    m=middleName[random.randint(0,len(middleName)-1)]
    return x+z+m

count=0
card=0
totalMoney=0
def shuaka():
    n=random.randint(0,500)
    global totalMoney
    totalMoney+=n
    for i in range(n):  # 一个人的 第几次
        global card
        card+=1
        time.sleep(0.01)
        print('%s刷卡1元,现在余额为：%s'%(getName(),card))

l=[]
for i in range(10):  #循环10次 创建了10个线程代表10个认
    count+=1
    l.append(threading.Thread(target=shuaka))

for i in l: #ｉ：　每一个线程对象
    i.start()

for i in l:
    i.join()

print(totalMoney)
