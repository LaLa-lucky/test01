# 根据年份判断生肖
chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'
# year = 2020
# year = int(input('请用户输入出生年份'))
# if (chinese_zodiac[year%12]) == '够':
#     print('鼠年的运势开头不好，后面会越来越好！！')
for cz in chinese_zodiac:
    print(cz)

for i in range(1,13):
    print(i)
for year in range(2000,2019):
    print('%s 年的生肖是 %s' % (year, chinese_zodiac[year % 12]))

    while True:
        print('a')
    # 中断死循环
        break