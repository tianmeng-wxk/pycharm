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
# n=10
# m=11
# sum =100
# print("1到{}到{}之和为：{}".format(n, m, sum))
# print("1到%d到%d之和为：%d"%(n, m, sum))
# print("之和为：",n,m,sum)
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
# dict = {'name':'aming','age':18,'school':'cema'}
# for i in dict.keys(),dict.values():
#     print(i)
# list=["name","pass","1","2"]
#
# dict={}
# dict = dict.fromkeys(list,"none")
# dict.pop("name")
# print(dict)
#
#
# a=10
# b=10
# print(a is b)
#
# a = input("请输入")
# list=[]
# i=0
# while i<10:
#     num = input("请输入第{}个数".format(i+1))
#     list.append(num)
#     i+=1
# list.sort(reverse=True)
# print(list)
# a=int(input("请输入一个整数："))
# b=int(input("请输入一个整数："))
# c=int(input("请输入一个整数："))
# if a+b>c and b+c>a and a+c>b:
#     if a==b==c:
#         print("等边三角形")
#     elif a==b or b==c or a==c:
#         print("等腰三角形")
#     else:
#         print("三角形")
#     zc = a+b+c
#     print("周长："+str(zc))
# else:
#     print("不能构成三角形")

# year = int(input("输入一个年份: "))
# if (year % 4) == 0:
#    if (year % 100) == 0:
#        if (year % 400) == 0:
#            print("{0} 是闰年".format(year))   # 整百年能被400整除的是闰年
#        else:
#            print("{0} 不是闰年".format(year))
#    else:
#        print("{0} 是闰年".format(year))       # 非整百年能被4整除的为闰年
# else:
#    print("{0} 不是闰年".format(year))

# a=input('请输入第一个数字')
# b=input('请输入第二个数字')
# print(a.isdigit())
#计算19000101距离现在（20190820）多少天
sum = 0
# for year in range(1900,2019):
#     if (year%4==0 and year%100!=0) or (year%400==0):
#         sum = sum + 366
#     else:
#         sum = sum + 365
#
# for month in range(1,9):
#     if month in [1,3,5,7,8,10,12]:
#         sum = sum + 31
#     elif month in [4,6,9,11]:
#         sum = sum + 30
#     else:
#         if (2019% 4 == 0 and 2019 % 100 != 0) or (2019 % 400 == 0):
#             sum = sum + 29
#         else:
#             sum = sum + 28
#
# print(sum-1)
# for i in range(1,6):
#     for j in range(0,i):
#         print('*', end='')
#     print()

# for i in range(0,5):
#     for j in range(5-i):
#         print("#",end='')
#     for e in range(0,i*2+1):
#         print("*",end='')
#     print()


# def eg(num1=10,num2=20):
#     return num2
# eg()
#
#
#
# def odd_number(ls):
#     list=[]
#     for i in range(1,len(ls),2):
#         a = ls[i]
#         list.append(a)
#     return list
# print(odd_number([34, 23, 52, 352, 352, 3523, 5]))

# def b(list):
#     if len(list)>5:
#         return list[:5]
#     else:
#         return list
# print(b([34,23,52,352,666,3523,5]))
# def d(*args):
#     sum=0
#     for i in args:
#         sum+=i
#     return sum
# print(d(1,2,4,6))
#
# def e(num1,num2,*args):
#     sum=num1*num2
#     return sum
# print(e(10,20))
#
# def a(num1,num2):
#     return max(num1,num2)
# print(a(10,20))
#文件夹批量重命名
import os
def rename(path):
    filename_list = os.listdir(path)
    print(filename_list)
    a = 0
    for i in filename_list:
       used_name = path + filename_list[a]
       print(used_name)
       # filename_list=filename_list[int(i)][:19]
       # print(filename_list)
       new_name = path + filename_list[a][:18]
       print(new_name)
       os.rename(used_name,new_name)
       a += 1
rename(r"C:\Users\Administrator\Desktop\test\3\\")










