import datetime,random, threading

KEYDICT = {601:'创建直播室', 602:'获取直播室数量',
           201:'进入直播室', 202:'获取个人信息', 203:'获取直播室信息', 204:'获取直播室人数',
           205:'发起聊天',206:'聊天', 209:'退出直播室'}

threading.TIMEOUT_MAX = 360

classroom = []
roomuser = {}

def chart_room():
    run = True
    entroom = ''
    threadid = threading.get_ident()
    while run:
        msg = input()
        try:
            code = eval(msg)
            if code == 601:
                room = random.randint(10000,99999)
                classroom.append(room)
                print(datetime.datetime.now(), ' 直播室 {} 创建成功'.format(room))
                roomuser[room] = 0
            elif code == 602:
                print(datetime.datetime.now(), ' 当前共有 {} 个直播室'.format(len(classroom)))
            elif code == 201:
                if len(classroom) > 0:
                    entroom = random.choice(classroom)
                    print(datetime.datetime.now(), ' 您当前进入的是 {} 号直播室'.format(entroom))
                    roomuser[entroom] = roomuser[entroom] + 1
                else:
                    print(datetime.datetime.now(), ' 对不起，当前没有活跃直播室，请先用 601 创建直播室')
            elif code == 202:
                print(datetime.datetime.now(), ' 您是第 {} 号用户，您当前在 {} 号直播室'.format(threadid, entroom))
            elif code == 203:
                print(datetime.datetime.now(), ' 您当前在 {} 号直播室'.format(entroom))
            elif code == 204:
                print(datetime.datetime.now(), ' 您当前在 {} 号直播室，当前共有 {} 个人员'.format(entroom, roomuser[entroom]))
            elif code == 209:
                run = False
        except BaseException as e:
            if entroom:
                print(datetime.datetime.now(), '{} 房间 {}Say:{}'.format(entroom, threadid, msg))
            else:
                print(datetime.datetime.now(), ' {}Say:{}'.format(threadid, msg))

t = threading.Thread(chart_room())
t.setDaemon(True)
t.start()