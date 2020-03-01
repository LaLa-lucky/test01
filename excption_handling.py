#
# #
# # try:
# #     year = int(input('input year:'))
# # except ValueError:
# #     print('年份要输入数字！！')
#
# try:
#     a = 123
#     a.append()
# except AttributeError:
#     print(' 数值没有属性append，只有list有append属性')
#
# # 默认异常类型为Excption
# try:
#     print(1/0)
# # 把提示信息给重命名成一个变量e,并且输出错误信息
# except Exception as e:
#     print('0不能作为除数 %s'%e)
# # 也可以自定义异常类型
# try:
#     raise NameError('helloError')
# except NameError:
#    print('我的自定义异常')
# finally:
#     print('最终总会执行的')
# 最终总会执行的操作  用finally
# try:
#     a = open('names.txt')
#     a.write('测试测试')
# except Exception as e:
#     print(e)
# finally:
#     a.close()
try:
    year = int(input('请输入年份'))
except ValueError:
    print('请输入数字！！')


