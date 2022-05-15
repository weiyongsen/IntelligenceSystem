import pymysql


def showOne(ip, id):
    # 打开数据库连接
    db = pymysql.connect(host=ip, user="root", password="00000000", database="IntelliSys")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    sql = "select user_id, user_number, user_name, user_position, user_img, user_gender from user where user_id=%d " % (
        id)
    cursor.execute(sql)
    data = cursor.fetchone()
    cursor.close()
    db.close()
    return data


def showAll(ip):
    # 打开数据库连接
    db = pymysql.connect(host=ip, user="root", password="00000000", database="IntelliSys")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    sql = "select * from user"
    cursor.execute(sql)
    data = cursor.fetchall()
    cursor.close()
    db.close()
    return data

ip = 'localhost'
print(showAll(ip))
