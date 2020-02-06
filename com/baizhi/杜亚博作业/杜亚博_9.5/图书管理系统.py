# 需求
# 1 书籍  2 管理员
# 配套的系统---管理书籍

# 登录，注册 --- 人
# 书籍管理界面---书

# 优先准备好数据库

# 人
userDB=[['abc','123'],
        ['admin','123'],
        ['zhang3','123']]
# 书
bookDB=[
        ['十万个为什么','不详',59.9,'科普','好看'],
        ['三体','刘慈欣',159.9,'科幻','比前一个好看'],
        ['钢铁是怎样炼成的','斯基',259.9,'励志小说','好看'],
        ['海底两万里','凡尔纳',139.9,'科幻小说','好看'],
        ['活着','余华',999.9,'文学小说','挺好看'],
        ['百年孤独','马尔克斯',99.9,'文学小说','好看'],
        ['时间简史','霍金',9.9,'科学文献','看不懂'],
        ['石头记','曹雪芹',59.9,'古典文学','好看'],
        ['斗破苍穹','天蚕土豆',20.0,'网络小说','悄悄看'],
        ['冰与火之歌','乔治',359.9,'魔幻巨作','好看'],]

# 构建界面
print('*********欢迎来到飞哥图书管理系统**********')
while 1:
    r=input('1.登录  2. 注册  3. 退出 \n')
    if r=='1':
        while 1:
            # 登录
            name=input('请输入用户名：\n')
            pwd=input('请输入密码：\n')
            # 判断是否在数据库
            flag=0
            for i in userDB:  # userDB： list   i：列表  i--e:str
                if i[0]==name and i[1]==pwd:
                    flag=1
                    break
            if flag==0:
                print('登录失败，请重新登录')
            else:
                print('登录成功')
                # 进入图书系统
                while 1:
                    print('**********欢迎'+str(name)+'进入图书系统***********')
                    r=input('1.查看所有书籍信息\n2.根据类别查询书籍\n3.根据价格区间查询书籍\n4.增加一本书籍\n5.修改一本书\n6.删除一本书\n7.退出系统\n')
                    if r=='1':
                        print('书名      作者     价格    类型    评价')
                        for i in bookDB:
                            print(i[0]+'\t'+i[1]+'\t'+str(i[2])+'\t'+i[3]+'\t'+i[4])
                    elif r=='2':
                        print('书的类型有 1科普  2科幻  3励志小说 4科幻小说 5文学小说 6科学文献 7古典文学 8网络小说 9魔幻巨作\n ')
                        n=int(input('请选择书籍类型\n'))
                        if n==1:
                            for i in bookDB:
                                if i[3]=='科普':
                                    print('书名            作者    价格    类型    评价')
                                    print(i[0] + '\t' + i[1] + '\t' + str(i[2]) + '\t' + i[3] + '\t' + i[4])
                        elif n==2:
                            for i in bookDB:
                                if i[3]=='科幻':
                                    print('书名            作者    价格    类型    评价')
                                    print(i[0] + '\t' + i[1] + '\t' + str(i[2]) + '\t' + i[3] + '\t' + i[4])
                        elif n==3:
                            for i in bookDB:
                                if i[3]=='励志小说':
                                    print('书名            作者    价格    类型    评价')
                                    print(i[0] + '\t' + i[1] + '\t' + str(i[2]) + '\t' + i[3] + '\t' + i[4])
                        elif n==4:
                            for i in bookDB:
                                if i[3]=='科幻小说':
                                    print('书名            作者    价格    类型    评价')
                                    print(i[0] + '\t' + i[1] + '\t' + str(i[2]) + '\t' + i[3] + '\t' + i[4])
                        elif n==5:
                            for i in bookDB:
                                if i[3]=='文学小说':
                                    print('书名            作者    价格    类型    评价')
                                    print(i[0] + '\t' + i[1] + '\t' + str(i[2]) + '\t' + i[3] + '\t' + i[4])
                        elif n==6:
                            for i in bookDB:
                                if i[3]=='科普':
                                    print('书名            作者    价格    类型    评价')
                                    print(i[0] + '\t' + i[1] + '\t' + str(i[2]) + '\t' + i[3] + '\t' + i[4])
                        elif n==7:
                            for i in bookDB:
                                if i[3]=='古典文学':
                                    print('书名            作者    价格    类型    评价')
                                    print(i[0] + '\t' + i[1] + '\t' + str(i[2]) + '\t' + i[3] + '\t' + i[4])
                        elif n==8:
                            for i in bookDB:
                                if i[3]=='网络小说':
                                    print('书名            作者    价格    类型    评价')
                                    print(i[0] + '\t' + i[1] + '\t' + str(i[2]) + '\t' + i[3] + '\t' + i[4])
                        elif n==9:
                            for i in bookDB:
                                if i[3]=='魔幻巨作':
                                    print('书名            作者    价格    类型    评价')
                                    print(i[0] + '\t' + i[1] + '\t' + str(i[2]) + '\t' + i[3] + '\t' + i[4])
                        else:print('输入错误')
                    elif r=='3':
                        print('书的价格区间有 1. <=50  2. 50<<100  3. 100<<200 4. 200<< \n')
                        n=int(input('选择价格区间\n'))
                        if n==1:
                            print('书名            作者    价格    类型    评价')
                            for i in bookDB:
                                if i[2]<=50.0:
                                    print(i[0] + '\t' + i[1] + '\t' + str(i[2]) + '\t' + i[3] + '\t' + i[4])
                        elif n==2:
                            print('书名            作者    价格    类型    评价')
                            for i in bookDB:
                                if i[2]>50.0 and i[2]<=100.0:
                                    print(i[0] + '\t' + i[1] + '\t' + str(i[2]) + '\t' + i[3] + '\t' + i[4])
                        elif n==3:
                            print('书名            作者    价格    类型    评价')
                            for i in bookDB:
                                if i[2]>100.0 and i[2]<=200:
                                    print(i[0] + '\t' + i[1] + '\t' + str(i[2]) + '\t' + i[3] + '\t' + i[4])
                        elif n==4:
                            print('书名            作者    价格    类型    评价')
                            for i in bookDB:
                                if i[2]>200:
                                    print(i[0] + '\t' + i[1] + '\t' + str(i[2]) + '\t' + i[3] + '\t' + i[4])
                        else:print('输入错误')
                    elif r=='4':
                        print('请输入书的信息')
                        book1=['书名','作者','价格','类型','评价']
                        book2=[]
                        for i in range(0,5):
                            if i==2:
                                a=float(input('输入价格'))
                                book2.append(a)
                            else:
                                a=input('输入'+book1[i])
                                book2.append(a)
                        bookDB.append(book2)
                        print('*******输入成功*******')
                    elif r=='5':
                        n=input('输入需要修改的书名\n')
                        f=0
                        for i in bookDB:
                            if i[0]==n:
                                f=1
                                print('书名      作者     价格    类型    评价')
                                print(i[0]+'\t'+i[1]+'\t'+str(i[2])+'\t'+i[3]+'\t'+i[4])
                                while 1:
                                    xiugai = int(input('0.修改书名 1.修改作者 2.修改价格 3.修改类型 4.修改评价 5.修改完成 返回\n'))
                                    if xiugai==0:
                                        n1=input('输入书名\n')
                                        i[0]=n1
                                        print('修改完成了')
                                    elif xiugai==1:
                                        n1=input('输入作者\n')
                                        i[1]=n1
                                        print('修改完成了')
                                    elif xiugai==2:
                                        n1=input('输入价格\n')
                                        i[2]=n1
                                        print('修改完成了')
                                    elif xiugai==3:
                                        n1 = input('输入类型\n')
                                        i[3] = n1
                                        print('修改完成了')
                                    elif xiugai==4:
                                        n1=input('输入评价\n')
                                        i[4]=n1
                                        print('修改完成了')
                                    elif xiugai==5:
                                        break
                                    else:
                                        print('输入错误')
                                        break

                        if f==0:
                            print('没有该书')
                    elif r=='6':
                        while 1:
                            n = input('输入需要删除的书名\n')
                            f=0
                            for i in bookDB:
                                if i[0] == n:
                                    f = 1
                                    print('书名      作者     价格    类型    评价')
                                    print(i[0] + '\t' + i[1] + '\t' + str(i[2]) + '\t' + i[3] + '\t' + i[4])
                                    bookDB.remove(i)
                                    print('删除成功')
                                    break
                            if f==0:
                                print('没有该书')
                    elif r=='7':
                        print('欢迎下次光临')
                        exit()

    elif r=='2':
        n1=input('输入用户名')
        def ist(i):
            if '~' in i or '!' in i or '@' in i or '#' in i or '$' in i or '%' in i or '^' in i or '&' in i or '*' in i or '-' in i or '=' in i or '[' in i or ']' in i or '\\' in i or ';' in i:
                return True
            else:
                return False
        while 1:
            p = input('请输入密码\n')
            n = len(p)
            a, b, c = 0, 0, 0
            a1 = 0
            x = p[0]
            if x.isalpha():
                a1 = 1
            for j in p:
                if j.isdecimal():
                    a = 1
                if j.isalpha():
                    b = 1
                if ist(j):
                    c = 1
            if n <= 8 or a == 1 and b == 0 or a == 0 and b == 1:
                print('等级为低')
            if a + b + c == 2 and n >= 8:
                print('等级为中')
            if a + b + c == 3 and n >= 16 and a1 == 1:
                print('等级为高')
                break
            if p == '':
                print('密码不能为空')
            if a1 == 0:
                print('必须字母开头')
            for i in range(10):
                if p.startswith('{0}'.format(i)):
                    print('不能以数字开头')
            if n < 16:
                print('长度不够，不能少于16位')
            if a + b + c < 3:
                print('需要由数字，字母及字符三种组合')
        u=[n1,p]
        userDB.append(u)
        print('注册成功')
    elif r=='3':
        print('欢迎下次光临')
        exit()
    else:
        print('输入有误，请重新输入')




