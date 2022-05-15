import pymysql


# 图像路径缺省未设置
def create(ip, pwd, name, position, img='0', gender=0):
    # 打开数据库连接
    db = pymysql.connect(host=ip, user="root",
                         password="00000000", database="IntelliSys")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    sql = "insert into user(user_pwd,user_name,user_position,user_img,user_gender) values('%s','%s'," \
          "%d,'%s',%d)" % (pwd, name, position, img, gender)
    try:
        cursor.execute(sql)
        db.commit()
        cursor.close()
        db.close()
        return '元组创建成功'
    except Exception:
        cursor.close()
        db.close()
        return '该元组已存在'

ip = 'localhost'
pwd = '123456'
name = 'wei'
position = 1
img = 'tupian'
gender = 0
print(create(ip, pwd, name, position, img, gender))
