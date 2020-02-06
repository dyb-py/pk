import re
# s = "ibaizhipython"
# rule = re.compile("baizhi")
# print(rule.match(s))

# search()
# print(rule.search(s))

# finditer
# s = "baizhi1baizhi2baizhi3"
# rule = re.compile("baizhi")
# result = rule.finditer(s)

# for i in result:
#     print(i)

# group()
# s = "baizhipython"
# rule = re.compile("baizhi")
# m = rule.match(s)
# print(m.group())

# start(),end(),span()
# s = "baizhipython"
# rule = re.compile("baizhi")
# m = rule.match(s)
# print(m)
# print(m.start(),m.end(),m.span())

## re模块  sub
# s = "baizhijiaoyuzhongguojiaoyushijiejiaoyu"
# print(re.findall("baizhi",s))
# print(re.sub("jiaoyu","niubi",s),s)
# print(re.subn("jiaoyu","牛逼",s))

# split()
s = "中国*北京+中关村软件园%百知教育"
# print(s.split("-"))
# print(re.split("-",s))
# print(re.split("[*,+,%]",s))