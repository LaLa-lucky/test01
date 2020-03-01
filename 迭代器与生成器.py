# iter() next()
# 把列表处理成迭代器
list1 = [1, 3, 4]
it = iter(list1)  # 用iter()转换成迭代器
print(next(it))
print(next(it))
print(next(it))
#print(next(it)) # 第四次会提示异常，停止迭代

# 迭代器 range 可以跟三个参数
# range (10,20,2) # 从10到20,每次取出一个数，加上步长

# for i in range(10, 20, 2):
#     print(i)
# 当range的步长为小数时，提示异常，range带的参数必须是整数


# 创建一个可以支持小数步数来增长的迭代器——生成器，需要自己构建迭代器时，使用yield
# 一个带有 yield 的函数就是一个 生成器
# 每执行到一个 yield 语句就会中断，并返回一个迭代值，下次执行时从 yield 的下一个语句继续执行
def frange(start, stop, step):  # 每次从start开始，加上step,小于stop
      x = start
      while x < stop:
        yield x  # 运行到这个位置，暂停并记录当前位置
        x += step

for i in frange(10, 20, 0.5):
    print(i)


# def abc():
#     yield 1
#     yield 2
#     yield 3
#     yield 4
#
# f = abc()
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))

