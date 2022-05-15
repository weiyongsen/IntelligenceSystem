import pymysql


def delete(ip, id):
    # 打开数据库连接
    db = pymysql.connect(host=ip, user="root", password="00000000", database="IntelliSys")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    sql = 'delete from user where user_id = %d' %(id)
    try:
        cursor.execute(sql)
        db.commit()
        cursor.close()
        db.close()
        return '删除成功'
    except Exception:
        cursor.close()
        db.close()
        return '代码错误'

ip = '127.0.0.1'
print(delete(ip,12))