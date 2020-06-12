import mysql.connector
def connect_mysql():
    ccon=mysql.connector.connect(
        host='localhost',
        user='root',
        password='wxk111',
        database='first'
    )
    print(ccon)
    cmd=ccon.cursor()
    # cmd.execute("show databases;")
    # for x in cmd:
    #     print(x)
    cmd.execute("select * from firsttable")
    res=cmd.fetchall()
    print(res)
    print(res[0][0])
connect_mysql()