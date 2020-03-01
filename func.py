# 函数以及函数传参的形式
#
# 实现只打印文本中奇数行的内容
f = open('names.txt', encoding='GB18030')
# 替换文本中的换行符为空格，用read().replace('','')方法
print(f.read().replace('\n', ' '))
# data = f.read()# i = 1
# # 逐行读取 用readlines()方法
# for line in f.readlines():
#     if i % 2 == 1:
#       print(line.strip('/n'))
#     i = i+1

