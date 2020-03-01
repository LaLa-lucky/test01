var1 = 123
def func():
    #在方法内部把变量作用域设为全局
   global var1
   var1 = 456
   print(var1)
#要记得调用函数才会执行
func()
print(var1)