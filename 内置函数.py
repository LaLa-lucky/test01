# python中常用的内建函数，常用在需要合并或者累加的操作中
# filter() 格式:filter(function,iterable) 这里的function可以用lambda格式来写
# map()
# reduce ()
# zip()

a = [1, 2, 3, 4, 5, 6, 7]
list(filter(lambda x: x > 2, a))  # 使用filter的lambda的形式 要把filter强制转换成list列表类型,否则lambda不会执行
print(a)

a = [1, 2, 3, 4, 5, 6, 7]
list(filter(lambda x: x > 2, a))

b = [4, 5, 6]
a =[1, 4, 2]
list(map(lambda x,y: x+y, a, b))

# zip函数 将字典里的key 和value对调  也可以用for in
dicta = {'a':'lala', 'b':'maichao'}
dictb = zip(dicta.values(),dicta.keys())
print(dict(dictb))

for i in zip((1, 2, 3),(4, 5, 6)):
    print(i)
