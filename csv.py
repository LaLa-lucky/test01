import  csv
with open('test.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['id', '辣辣', '17621977523'])
    writer.writerow(['01', 'zhangsan', '13600000001'])
    writer.writerow(['02', 'lisi', '13600000002'])
    writer.writerow(['03', 'wangwu', '13600000003'])
