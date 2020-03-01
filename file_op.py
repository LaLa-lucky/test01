# 写入到一个文件
# 步骤1:先创建文件，定义好模式
# 步骤2:用write方法写入字符串
# 步骤3:关闭该文件
# file1 = open('names.txt', 'w')
# file1.write('周权诸葛亮')
# file1.close()
#
# # 读取文件,默认模式为读，不用加r
# file2 = open('names.txt')
# print(file2.read())
# file1.close()
#
# #  向文件添加内容
# file3 = open("names.txt", 'a')
# print(file3.write("你好稍安勿躁"))
# file3.close()

# 只读取一行内容,用readline
# file4 = open("names.txt")
# print(file4.readline())
# # 逐行读取，需要用for循环，用readlines
# file5 = open("names.txt")
# for line in file5.readlines():
#     print(line)
#     print("===========")
# 处理完文件之后，回到文件开头继续处理
# 刚开始打开文件，指针在文件开头
file6 = open("names.txt")
print('当前文件的指针的位置 %s'%file6.tell())
# 只读取一个字符 用read(1)
print('当读取了一个字符时，读到的内容是:%s' %file6.read(1))
print('当前指针的位置是 %s'%file6.tell())
# 让指针位置回到0  用seek
file6.seek(0)
print('指针回到文件开头时，指针位置：%s'%file6.tell())
# seek支持两个参数，第一个参数代表偏移位置，第二个参数 为0时表示从文件开头偏移，为1表示从当前位置偏移，为2表示从文件结尾
file6.seek(5,0)
print(file6.tell())