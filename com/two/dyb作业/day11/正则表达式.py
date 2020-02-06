import re
# s1 = "我爱你你爱他他不爱你滚犊子"
# rule = "他"
# print(re.findall(rule,s1))
# s1 = "accabcabc"
# tel = '010-32345678'
# print(re.findall("010-[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]",tel))

# # ^
# s1 = "a^bcaicadc"
# rule = "a\^bc"
# print(re.findall(rule,s1))

#结合
# s1 = "yabcaicadca^c"
# rule = "a[b,^]c"
# print(re.findall(rule,s1))

# $
# s1 = "adw/123/ad"
# rule = "adw/\d{1,3}"
# print(re.findall(rule,s1))

# 结合
# s1 = "yabcaicadcacab"
# rule = "a[b$c]"
# print(re.findall(rule,s1))

# 不出现在行尾
# s1 = "a$bcaicadc"
# rule = "a\$bc"
# print(re.findall(rule,s1))

# \
# s1 = "010-12345678"
# rule = "010-\d\d\d\d\d\d\d"
# print(re.findall(rule,s1))

# s1 = "hello\tworld"
# rule = "\s"
# print(re.findall(rule,s1))

# \本身
# s1 = r"hello\我"
# rule = r"\\"
# print(re.findall(rule,s1))

# *
# s1 = "010-123211"
# rule = "010-\d*"
# print(re.findall(rule,s1))

# +
# s1 = "010-1345335"
# rule = "010-\d+"
# print(re.findall(rule,s1))

# .
# s1 = "hellobaizhi\rcom"
# rule = "hellobaizhi.com"
# print(re.findall(rule,s1))

# ?
# s1 = "010-"
# rule = "010-\d?"
# print(re.findall(rule,s1))

# 组合
# s1 = "abcabcabcabc"
# rule = ".+?"
# print(re.findall(rule,s1))

s = "010-12345678"
rule = "\d{3}-\d{8}"
print(re.findall(rule,s))

# s = "010-1234"
# print(re.findall("010-\d{4,10}",s))


# s = "010-12344657"
# rule = "010-\d+"
# re_compile = re.compile(rule)
# print(re_compile.findall(s))

# match()
