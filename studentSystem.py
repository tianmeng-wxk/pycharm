list = ["关羽", "张飞", "赵云", "刘备", "周瑜", "诸葛亮", "庞统"]
print(list)
print("""
# ---------学生管理系统 - -------
# 0 - -显示所有学生名字
# 1 - -增加学生名字
# 2 - - 删除学生名字
# 3 - --修改学生名字(根据学生的id编号删除，id从1开始)
# 4 - --退出程序
# -----------------------------""")
while True:
    try:
        usr_num = int(input("请输入操作编号(1-4)"))
        if usr_num == 0:
            for i in list:
                print(i)
        elif usr_num == 1:
            add_name = input("请输入增加人物的姓名:")
            list.append(add_name)
            print("增加人物的姓名成功，增加后的人物姓名如下:", list)
        elif usr_num == 2:
             del_name= input("请输入要删除的人物姓名：")
             for i in list:
                 if i == del_name:
                     list.remove(del_name)
                     print("删除人物的姓名成功，删除后的人物姓名如下:", list)
                     break
             else:
                 print("你输入的人物姓名不存在")


        elif usr_num == 3:
            modify_id = int(input('请输入你要修改的人物的编号：'))
            # 编号--》列表里面元素的个数是有关系的 len()判断列表元素个数
            if 0 < modify_id <= len(list):
                modify_name = input("请输入新名字:")
                modify_index = modify_id - 1
                list[modify_index] = modify_name
                print("修改成功",list)
            else:
                print("你输入的学生编号不对")

        else:
            print("退出系统成功")
    except Exception as e:
        print("输入错误")