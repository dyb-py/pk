def ist(i):
    if '~'in i or '!'in i or '@'in i or '#'in i or '$'in i or '%'in i or '^'in i or '&'in i or '*'in i or '-'in i or '='in i or '['in i or ']'in i or '\\'in i or ';'in i:
        return True
    else:return False
while 1:
    p=input('请输入需要检查的密码组合\n')
    n=len(p)
    a,b,c=0,0,0
    a1=0
    x=p[0]
    if x.isalpha():
        a1=1
    for j in p:
        if j.isdecimal():
            a=1
        if j.isalpha():
            b=1
        if ist(j):
            c=1
    if n<=8 or a==1 and b==0 or a==0 and b==1:
        print('等级为低')
    if a+b+c==2 and n>=8:
        print('等级为中')
    if a+b+c==3 and n>=16 and a1==1:
        print('等级为高')
        exit()
    if p=='':
        print('密码不能为空')
    if a1==0:
        print('必须字母开头')
    for i in range(10):
       if p.startswith('{0}'.format(i)):
           print('不能以数字开头')
    if n<16:
        print('长度不够，不能少于16位')
    if a+b+c<3:
        print('需要由数字，字母及字符三种组合')