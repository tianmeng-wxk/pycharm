'''写入文件'''
import tablib
'''准备数据'''
headers = ["url", "method", "expected"]
data_list = [
    ["http://www.baidu.com", "get", "success"],
    ["http://www.m.baidu.com", "post", "fail"]
]
data = tablib.Dataset(*data_list, headers=headers, title='测试用例')
data.append(["http://www.baidu.com", "get", "success"])
data.append_col(['pass', 'pass', 'pass'], header='result')
print(data)
'''打开文件'''
f = open('C:/Users/Administrator/Desktop/data.xlsx', mode='wb')
'''写入数据'''
f.write(data.xlsx)
'''关闭文件'''
f.close()

