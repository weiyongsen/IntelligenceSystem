import pymysql


def create(ip, name):
    # 打开数据库连接
    db = pymysql.connect(host=ip, user="root",
                         password="00000000", database="IntelliSys")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    sql = """
            CREATE TABLE %s (
            `user_id` int(11) NOT NULL AUTO_INCREMENT,
            `user_name` varchar(15) NOT NULL,
            `user_position` int(11) NOT NULL,
            `user_pwd` varchar(20) NOT NULL,
            `user_img` varchar(200) NOT NULL,
            `user_gender` int(11) NOT NULL DEFAULT '0',
            PRIMARY KEY (`user_id`)
            ) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;
        """ %(name)
    try:
        cursor.execute(sql)
        db.commit()
        cursor.close()
        db.close()
        return '表格创建成功'
    except Exception:
        cursor.close()
        db.close()
        return '表格已存在'


def drop(ip, name):
    # 打开数据库连接
    db = pymysql.connect(host=ip, user="root",
                         password="00000000", database="IntelliSys")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    sql = """
            DROP TABLE %s;
        """  %(name)
    try:
        cursor.execute(sql)
        db.commit()
        cursor.close()
        db.close()
        return '表格删除成功'
    except Exception:
        cursor.close()
        db.close()
        return '表格不存在'


ip = 'localhost'
print(create(ip,'user'))
# print(drop(ip,'user'))
