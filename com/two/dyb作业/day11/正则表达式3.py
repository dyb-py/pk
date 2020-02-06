import re
# s = "baizhi\ncom"
# print(re.findall("baizhi.com",s,re.S))

#  I
# s = "BaizhiJIAoyu"
# print(re.findall("baizhijiaoyu",s,re.I))

# s = """
# today
# yesterday
# tomorrow
# """
# rule = "^today$"
# print(re.findall(rule,s,re.M))

# s = "010-12345678"
# # rule = "\d{3,4}-?\d+"
# rule = """
# \d{3,4}
# -?
# \d+
# """
# print(re.findall(rule,s,64))

# s1 = "taobao@888.com"
# s2 = "jd16543@662.cn"
# s3 = "python@niubi.org"
# s4 = "wenguang@zpark.net"
# rule = "(\w+@\w+\.)(com|cn)"
# print(re.findall(rule,s1))
# print(re.findall(rule,s2))
# print(re.findall(rule,s3))
# print(re.findall(rule,s4))


# s = """
# this day
# a = 123
# a = hello a = nihao
# world
# """
# print(re.findall("a = (\w+)",s))