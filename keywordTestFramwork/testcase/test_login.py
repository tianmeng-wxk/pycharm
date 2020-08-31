# 用unittest组织测试用例
from actions.keywords import *
from utils.excelUtil import ExcelUtil

excel_path = '../data/某某模块的测试用例集.xlsx'
operator_id = 1
operator_name = 2
keyword = 3
loc_type = 4
loc_ex = 5
oprator_value = 6
result = 7

def test_login():
    excel = ExcelUtil(excel_path)
    for rownum in range(2, excel.get_max_row() + 1):
        keyword1 = excel.get_cell_value(rownum, keyword)
        loc_type1 = excel.get_cell_value(rownum, loc_type)
        loc_ex1 = excel.get_cell_value(rownum, loc_ex)
        oprator_value1 = excel.get_cell_value(rownum, oprator_value)
        if loc_type1== loc_ex1 == oprator_value1 ==None:
            func = keyword1 + "()"
        elif oprator_value1 ==None:
            # func = keyword1 + "(loc_type1, loc_ex1)"
            # click("class name", "login_btn")
            func ='%s("%s", "%s")' % (keyword1, loc_type1, loc_ex1)
        elif loc_type1== loc_ex1 == None:
            # 只有value有值, 一个参数的方法
            func = '%s("%s")' % (keyword1, oprator_value1)
        else:
            # 都不为空,需要传3个参数
            func = '%s("%s", "%s", "%s")' % (keyword1, loc_type1, loc_ex1, oprator_value1)

        eval(func)


if __name__ == '__main__':
    test_login()
