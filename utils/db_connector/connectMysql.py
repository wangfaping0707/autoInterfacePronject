from utils.configparserUtil import ConfigparserReader
import pymysql
from utils.log_tool.log_tool import logger
conf = ConfigparserReader(r'D:\InterAutoTest_W\data\config.ini')


# print(conf.get_mysql_conf('charset'))

class ConnectMysql:
	"""链接数据库，进行增删改查操作"""

	def __init__(self):
		self.db_info = {
			'host': conf.get_mysql_conf('host'),
			'poat': int(conf.get_mysql_conf('port')),
			'user': conf.get_mysql_conf('user'),
			'password': conf.get_mysql_conf('password'),
			'charset': conf.get_mysql_conf('charset'),
			'database': conf.get_mysql_conf('database')
		}

		try:
			# 创建数据库链接对象
			self.db = pymysql.connect(**self.db_info)
			# 创建SQL游标对象，游标对象主要用来执行SQL语句
			# pymysql.cursors.DictCursor：将数据库查询结果以字典形式返回
			self.cursor = self.db.cursor(pymysql.cursors.DictCursor)
			logger.info('数据库成功链接')
		except Exception as e:
			logger.error('数据库链接失败')
			raise e

	def close(self):
		"""关闭数据链接对象 和 数据库游标对象"""
		if self.cursor:
			self.cursor.close()
		if self.db:
			self.db.close()
		return True

	def query(self, sql, fetchall=False):
		"""
		查询数据库中的数据
		:param sql: 查询的SQL语句
		:param fetchall: 查询全部数据，默认值为False，查询单条数据
		:return:
		"""
		try:
			self.cursor.execute(sql)
			"""
			在使用pymysql执行SQL查询时，通常不需要执行commit()，因为查询操作默认不会改变数据库状态，
			它只是读取数据。commit() 方法用于在数据库中进行更改，例如插入、更新或删除操作之后，将这些更改永久保存到数据库中。
			self.db.commit()
			"""
			if fetchall:
				res = self.cursor.fetchall()
			else:
				res = self.cursor.fetchone()
			return res
		except Exception as e:
			logger.error('查询数据库内容出现异常')
			raise e
		finally:
			self.close()

	def delete(self, sql):
		"""
		删除数据库内容
		:param sql: 删除sql语句
		:return:
		"""
		try:
			# 游标对象主要用来执行SQL语句
			self.cursor.execute(sql)
			# commit()方法用于在数据库中进行更改，例如插入、更新或删除操作之后，将这些更改永久保存到数据库中。
			self.db.commit()
		except Exception as e:
			# sql执行报错，就需要进行数据回滚
			self.db.rollback()
			logger.error('删除SQL执行异常')
			raise e
		finally:
			self.close()

	def update(self, sql):
		"""
		更新数据库内容
		:param sql: 更新数据库内容的sql语句
		:return:
		"""
		try:
			# 游标对象主要用来执行SQL语句
			self.cursor.execute(sql)
			# commit()方法用于在数据库中进行更改，例如插入、更新或删除操作之后，将这些更改永久保存到数据库中。
			self.db.commit()
		except Exception as e:
			# sql执行报错，就需要进行数据回滚
			self.db.rollback()
			logger.error('更新SQL执行异常')
			raise e
		finally:
			self.close()

	def insert(self, sql):
		"""
		新增数据库内容
		:param sql: 新增数据库内容的sql语句
		:return:
		"""
		try:
			# 游标对象主要用来执行SQL语句
			self.cursor.execute(sql)
			# commit()方法用于在数据库中进行更改，例如插入、更新或删除操作之后，将这些更改永久保存到数据库中。
			self.db.commit()
		except Exception as e:
			# sql执行报错，就需要进行数据回滚
			self.db.rollback()
			logger.error('新增SQL执行异常')
			raise e
		finally:
			self.close()
