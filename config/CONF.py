import os

# 获取当前文件所在路径    os.sep 获取本机操作系统所用分隔符
# base_path = os.path.abspath(__file__)
# print(f'base_path:{base_path}')
from utils import YamlUtil

current_path = __file__
# print(f'current_path:{current_path}')
# 获取当前文件所在最上层目录
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
# 获取config目录所在路径
_config_path = BASE_DIR + os.sep + 'config'

# 获取data目录所在路径
_data_path = BASE_DIR + os.sep + 'data'

# 获取conf.yml文件所在路径
_config_file = _config_path + os.sep + 'conf.yml'
# 定义logs目录路径
_logs_path = BASE_DIR + os.sep + 'logs'
# 定义数据库配置文件路径
_db_path = _config_path + os.sep + 'db_conf.yml'

# 定义testlogin.yml-文件路径
_data_file_path = _data_path + os.sep + 'testlogin.yml'

# 定义data1.xlsx-文件的路径
_data1_excel_file_path = os.path.join(_data_path, 'data1.xlsx')


# _config_path 和 _conf_file被定义成了私有变量，所以需要定义函数返回路径
def get_config_path():
	return _config_path


# 获取conf.yml配置文件
def get_config_file():
	return _config_file


# 获取logs目录路径
def get_logs_path():
	return _logs_path


# 获取db_conf.yml配置文件
def get_db_conf():
	return _db_path


# 获取testlogin.yml配置文件
def get_testlogin_file():
	return _data_file_path


# 获取data1.xlsx配置文件
def get_excel_data1():
	return _data1_excel_file_path


# 读取配置文件
class ConfigYaml():
	def __init__(self):
		self.config = YamlUtil.YamlReader(get_config_file()).read_yaml()
		self.db_config = YamlUtil.YamlReader(get_db_conf()).read_yaml()

	# 定义方法获取需要的信息
	def get_config_url(self):
		return self.config[0]['Base']['fat']['url']

	# 获取excel文件名称
	def get_excel_file(self):
		"""
		获取测试用例excel名称
		:return:
		"""
		return self.config[0]['Base']['fat']['case_excel_file']

	# 获取sheet表格名称
	def get_excel_sheet(self):
		"""
		获取测试用例sheet名称
		:return:
		"""
		return self.config[0]['Base']['fat']['sheet_name']

	# 获取日志级别
	def get_config_log_level(self):
		return self.config[0]['Base']['log_level']

	# 获取日志文件扩展名
	def get_config_log_extention(self):
		return self.config[0]['Base']['log_extension']

	def get_db_config_info(self, db_alias):
		"""
		根据 db_alias 获取详细数据库信息
		:param db_alias:
		:return:
		"""
		return self.db_config[0][db_alias]

	# 返回邮箱信息
	def get_email_info(self):
		return self.config[0]['email']


if __name__ == '__main__':
	config_info = ConfigYaml().get_config_url()
	print(config_info)
	print(ConfigYaml().get_config_log_level())
	print(ConfigYaml().get_config_log_extention())
	print(ConfigYaml().get_db_config_info('db_1'))
	print(ConfigYaml().get_excel_file())
	print(ConfigYaml().get_excel_sheet())
	print('----------------')
	print(ConfigYaml().get_email_info())
