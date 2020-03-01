zodiac_name = (u'摩羯座', u'水瓶座', u'双鱼座',  u'白羊座',  u'金牛座',
               u'双子座',  u'巨蟹座',  u'狮子座', u'处女座', u'天秤座', u'天蝎座', u'射手座')
zodiac_days = ((1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22), (7, 23),
                (8, 23), (9, 23), (10, 23), (11, 23), (12, 23))
chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'


# 把上面的信息放入字典里面，先对字典初始化，最后再往里面填充内容
cz_num = {}
for x in chinese_zodiac:
    cz_num[x] = 0

zn_num = {}
for z in zodiac_name:
    zn_num[z] = 0
while True:
    #  用户输入月份和日期
    int_month = int(input('请输入月份：'))
    int_day = int(input('请输入日期：'))
    int_year = int(input('请输入年份'))
    n = 0
    while zodiac_days[n] < (int_month, int_day):
        if int_month == 12 and int_day > 23:
            break
    n += 1
    print(zodiac_name[n])

    sx = chinese_zodiac[int_year % 12]

    cz_num[sx] += 1
    zn_num[zodiac_name[n]] += 1

    for i in cz_num.keys():
        print('生肖 %s 有 %d 个' % (i, cz_num[i]))
        
    for i in zn_num.keys():
        print('星座 %s 有 %d 个' % (i, zn_num[i]))












