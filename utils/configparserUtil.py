from configparser import ConfigParser
import os


class ConfigparserReader:
	def __init__(self, file):
		if os.path.exists(file):
			self.file = file
			self.cfg = ConfigParser()
		else:
			raise FileNotFoundError('文件不存在')

	# 读取传入的配置文件
	def read_config(self):
		self.cfg.read(self.file)

	# 获取指定区域、指定值,如：cfg.get('Database', 'host')
	def get_info(self, section, option):
		self.read_config()
		return self.cfg.get(section, option)

	# 返回Host的信息
	def get_Host_conf(self, option):
		return self.get_info('Host', option)

	# 返回数据库的信息
	def get_mysql_conf(self, option):
		return self.get_info('Mysql', option)


if __name__ == '__main__':
	cr = ConfigparserReader(r'../data/config.ini')
	print(cr.get_mysql_conf('host'))
	print(cr.get_mysql_conf('port'))
