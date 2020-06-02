list = ["天梦", "熊", "张三", "李四", "王五"]
print("""
---------欢迎进入T666班学生管理系统 - -------
请选择系统功能：
0:显示所有学员信息
1:添加一个学员信息
2:删除一个学员信息
3:修改一个学员信息
4:查询一个学员信息
exit:退出学生管理系统
""")
while True:
    try:
        stu_num = int(input("请输入操作编号0~4或者exit"))
        if stu_num == 0:
            print(list)
        elif stu_num == 1:
            add_name = input("请输入增加人的姓名：")
            list.append(add_name)
            print(list)
        elif stu_num == 2:
             del_name= input("请输入删除人的姓名：")
             for i in list:
                 if i == del_name:
                     list.remove(del_name)
                     print(list)
                     break
             else:
                 print("你要删除的人不存在")#作业不要求


        elif stu_num == 3:
            # modify_id = int(input('请输入你要修改的人物的编号：'))
            # # 编号--》列表里面元素的个数是有关系的 len()判断列表元素个数
            # if 0 < modify_id <= len(list):
            #     modify_name = input("请输入新名字:")
            #     modify_index = modify_id - 1
            #     list[modify_index] = modify_name
            #     print("修改成功",list)
            # else:
            #     print("你输入的人物编号不对")
            update_name = input("请输入你要修改人的姓名")
            for i in list:
                if i == update_name:
                    new_name = input("请输入需要修改后的姓名")
                    index = list.index(update_name)
                    list[index] = new_name
                    print(list)
                    break
            else:
                print("T666班没有这个学员")

        elif stu_num ==4:
            selete_name = input("请输入查询人的姓名：")
            for i in list:
                if i == selete_name:

                    print("{}在座位号{}的位置:".format(selete_name,list.index(selete_name)))
                    break
            else:
                print("T666班没有这个学员")

        elif stu_num == "exit":
            print("exit欢迎使用T666的学生管理系统，下次再见。")

    except Exception as e:
        print("exit欢迎使用T666的学生管理系统，下次再见。")
        break