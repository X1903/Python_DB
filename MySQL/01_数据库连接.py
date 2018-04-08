import MySQLdb

# 获取连接
try:
    connt =  MySQLdb.connect(
        host='127.0.0.1',
        user='root',
        passwd='q8022761',
        db='news',
        port=3306,
        charset='utf8'
    )

    # 获取数据
    cursor = connt.cursor()
    cursor.execute("select * from news order by created_at desc;")

    rest = cursor.fetchone()
    print(rest)

    # 关闭连接
    connt.close()
except MySQLdb.Error as e:
    print("Error %d: %s" % (e.args[0], e.args[1]))

