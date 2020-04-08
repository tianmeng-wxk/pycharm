import tablib
import openpyxl
import xlrd
f = open('C:/Users/Administrator/Desktop/data.xlsx', mode='rb')
data = tablib.import_set(f.read(), 'xlsx')
f.close()
print(data[0:3])
print(data["url"])