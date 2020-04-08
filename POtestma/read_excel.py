import xlrd

def dict_data(file_path, sheet_name):
    workbook = xlrd.open_workbook(file_path)
    worksheet = workbook.sheet_by_name(sheet_name)
    if worksheet.nrows <= 1:
        print("表格数据小于等于1行，表格不合规")
    else:
        list = []
        headers = worksheet.row_values(0)
        for i in range(1, worksheet.nrows):
            dict = {}
            values = worksheet.row_values(i)
            for x in range(worksheet.ncols):
                dict[headers[x]] = values[x]
            list.append(dict)
        return list
if __name__ == '__main__':
    file_path = "C:/Users/Administrator/Desktop/testma.xlsx"
    sheet_name = "Sheet1"
    print(dict_data(file_path, sheet_name))








