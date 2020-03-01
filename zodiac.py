# 元组 ——记录十二生肖，根据年份来判断生肖（序列）
chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'
# 写 下标 序列的切片操作
# print(chinese_zodiac[0:6])

# 可以从后往前访问
# print(chinese_zodiac[-1])
year = 2020
print(year%12)
print(chinese_zodiac[year%12])
print('狗' in chinese_zodiac)
print('猫' in chinese_zodiac)
print(chinese_zodiac + '辣辣属狗属猪？')
print(chinese_zodiac * 5)


zodiac_name = (u'摩羯座', u'水瓶座', u'双鱼座',  u'白羊座',  u'金牛座', u'双子座',
               u'双子座',  u'巨蟹座',  u'狮子座', u'处女座', u'天秤座', u'天蝎座', u'射手座')
zodiac_days = ((1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22), (7, 23),
              (8, 23), (9, 23), (10, 23), (11, 23), (12, 23))
(month, day) = (8, 12)
zodiac_day = filter(lambda x: x <= (month, day), zodiac_days)
print(zodiac_day)

zodiac_len = len(list(zodiac_day)) % 12
print(zodiac_name[zodiac_len])

# 列表的运用  列表是中括号，元组是括号，字符串是双引号
a_list = ['lala', 'maichao']
a_list.append('baobao')
a_list.remove('baobao')
print(a_list)


