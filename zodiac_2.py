zodiac_name = (u'摩羯座', u'水瓶座', u'双鱼座',  u'白羊座',  u'金牛座',
               u'双子座',  u'巨蟹座',  u'狮子座', u'处女座', u'天秤座', u'天蝎座', u'射手座')
zodiac_days = ((1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22), (7, 23),
                (8, 23), (9, 23), (10, 23), (11, 23), (12, 23))
# 用户输入月份和日期
int_month = int(input('请输入月份：'))
int_day = int(input('请输入日期：'))
# 这里的range(len)等于range(12)的作用
# for i in range(len(zodiac_days)):
#     # 从元组里遍历找到第一个大于用户输入的
#     if zodiac_days[i] >= (int_month, int_day):
#         # 通过列表的形式，每次循环的i都不一样
#         print(zodiac_name[i])
#         break
#     elif int_month == 12 and int_day > 23:
#         print(zodiac_name[0])
#     # 此处不加break 会执行i次也就是12次循环比较
#         break
n = 0
while zodiac_days[n] < (int_month, int_day):
    # if int_month == 12 and int_day > 23:
    #     break
    #     # break后面的+1不会执行
    n += 1
print(zodiac_name[n])




































# zodiac_day = filter(lambda x: x <= (month, day), zodiac_days)
# print(zodiac_day)
# zodiac_len = len(list(zodiac_day)) % 12
# print(zodiac_name[zodiac_len])











