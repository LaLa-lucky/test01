# atest = ['句字', '基督教', '发奖金']
# b = 123456
# print(b.len())
def  func(a,b,c):
    print('a等于 %s' %a)
    print('b等于 %s' %b)
    print('c等于 %s' %c)
# %的作用是值的替换，不管值的类型是什么
#func('123', 4, 66)
func(a=2,b='11',c=333)

# 函数的可变长参数。参数可以在前面加一个*号
# 取得参数的个数,只有first是固定的参数，后面的参数的长度是可变的
def howlong(first,*other):
     print( 1 + len(other))
howlong(123,234,456,'第四个')