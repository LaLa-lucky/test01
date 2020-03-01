#   求1到10所有偶数的平方
alist = []
for i in range(1,11):
    if (i % 2 ==0):
      alist.append( i*i)
print(alist)

# 列表推导式实现
blist = [i*i for i in range(1, 11) if (i % 2) == 0]
print(blist)

# 字典推导式实现
chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'
cz_num = {}
for x in chinese_zodiac:
  cz_num[x] = 0
#  for实现字典推导式  实现上述
cz_num = {x: 0 for x in chinese_zodiac}


