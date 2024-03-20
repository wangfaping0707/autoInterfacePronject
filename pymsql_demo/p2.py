import pymysql

"""
在PyMysql库中可以使用fetchone()方法来读取，fetchone()方法每次可以从表中获取一条数据记录
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
sql = "select * from actor"
# 使用execute()方法执行sql语句
cursor.execute(sql)
# 使用fetchone()方法一次性获取一条数据
for i in range(5):
	res = cursor.fetchone()
	# res = cursor.fetchmany(2)
	# 打印获取到的数据
	print(res)

# 关闭游标对象
cursor.close()
# 关闭database对象
db.close()
