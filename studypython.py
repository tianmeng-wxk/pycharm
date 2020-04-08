# '''def 代码实现测试用例的编写(str):
#     print("str")
#     return str
#     代码实现测试用例的编写("1",str)'''
# str="hello"
# #print(str[-1])
# #str[0] = "l"
# print(str)
# student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
# print(student)
# dict = {}
# dict["one"] = 1
# dict['two'] = "二"
# print(dict["one"])
# print(dict)
# jihe = set()
# jihe.add("a")
# jihe.add("b")
# print(jihe)
# list = []
# list.insert(0,"x")
# print(list)
# list.insert(1,"y")
# print(list)
# list.insert(0,"z")
# print(list)
# def test():
#     print("hello world")
# test()
# '''
# '''
# n = 100
#
# sum = 0
# counter = 1
# while counter <= n:
#     sum = sum + counter
#     counter += 1
#
# print("1 到 %d 之和为: %d" % (n, sum))
#
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         print("实例化类时，init方法就被调用了")
#
# p = Person("tom", 22)
# print(p.name)
# print(p.age)
# import time
# localtime = time.asctime(time.localtime(time.time()))
# print(localtime)
# print(time.strftime("%b %Y-%m-%d %H:%M:%S ",time.localtime()))
# import calendar
# cal = calendar.month(2019,1)
# print(cal)
# import json
# data = {
#     "name" : "wang",
#      "age" : 15
# }
# json_str = json.dumps(data)
# print(json_str)
# json_str2 = json.loads(json_str)
# print(json_str2["name"])
#
# with open('C:/Users/Administrator/Desktop/data.json', 'w') as f:
#     json.dump(data, f)
#
# # 读取数据
# with open('C:/Users/Administrator/Desktop/data.json', 'r') as f:
#     data = json.load(f)
#
# # alist = [1, 3, 5, 7, 9, 34]
# # sum = 0
# # for i in range(0, len(alist)):
# #     sum += alist[i]
# # print(sum)
# '''测试用例工具tablib'''
# import tablib
# headers = ["url", "method", "expected"]
# data_list = [
#     ["http://www.baidu.com", "get", "success"],
#     ["http://www.m.baidu.com", "post", "fail"]
# ]
# data = tablib.Dataset(*data_list, headers = headers, title="testcase")
# print(data)
#
# f = open("data.xlsx", mode="wd")
# f.write(data.xlsx)
# f.close()

'''---------------------------'''
for i in range(5):
    #print("这是i:", i)
    for x in range(5):
        print("这是x:", x)



