import pymysql
from utils.LogUtil import my_log

# 创建链接数据库工具类
class Mysql:
	# 初始化数据库链接对象
	def __init__(self, host, user, password, database, charset='utf8', port=3306):
		self.log = my_log()
		self.db = pymysql.connect(
			host=host,
			user=user,
			password=password,
			database=database,
			charset=charset,
			port=port
		)
		# 创建读取sql的游标对象
		self.cursor = self.db.cursor(pymysql.cursors.DictCursor)

	# 创建读取数据的方法
	# 读取一条数据
	def fetchone(self, sql):
		# 执行查询sql语句
		self.cursor.execute(sql)
		# 返回查询结果
		return self.cursor.fetchone()

	# 读取若干条数据
	def fetchmany(self, sql, num):
		# 执行查询sql语句
		self.cursor.execute(sql)
		# 返回查询结果
		return self.cursor.fetchone(num)

	# 读取所有数据
	def fetchmany(self, sql):
		# 执行查询sql语句
		self.cursor.execute(sql)
		# 返回查询结果
		return self.cursor.fetchall()

	# 数据写入数据库的方法
	def exec(self, sql):
		try:
			if self.db and self.cursor:
				self.cursor.execute(sql)
				self.db.commit()
		except Exception as f:
			# sql执行报错，就需要进行数据回滚
			self.db.rollback()
			# 打印报错信息
			self.log.error('mysql 执行失败！')
			self.log.error(f)
			return False
		return True

	def close_obj(self):
		# 关闭游标对象
		if self.cursor is not None:
			self.cursor.close()
		# 关闭数据库链接对象
		if self.db is not None:
			self.db.close()















