import pymysql

"""
在PyMysql库中可以使用execute()方法执行insert into语句来实现
"""
# 创建数据库对象
db = pymysql.connect(
	host="localhost",
	user="root",
	passwd="123456",
	database="sakila",
	charset="utf8",
	port=3306
)
# 创建sql游标对象，游标对象主要用来执行sql语句
# cursor = db.cursor()
cursor = db.cursor(pymysql.cursors.DictCursor)
# 要执行的sql语句
sql = "INSERT INTO actor(`actor_id`, `first_name`, `last_name`, `last_update`) VALUES ('202', '仙林', '陈', '2023-11-26 21:35:33')"
# 使用execute()方法执行sql语句
cursor.execute(sql)
# 默认情况下mysql的事物机制是开启的，需要使用commit()方法进行数据提交
db.commit()

# 关闭游标对象
cursor.close()
# 关闭database对象
db.close()
