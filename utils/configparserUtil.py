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
		return self.cfg.get(section, option)

	# 获取ip地址
	def get_host(self):
		self.read_config()
		ip = self.get_info('Host', 'host')
		return ip


if __name__ == '__main__':
	cr = ConfigparserReader(r'../data/config.ini')
	print(cr.get_host())
