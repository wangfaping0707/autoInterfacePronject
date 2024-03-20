import datetime
import logging
import os

from config.CONF import ConfigYaml

# 定义日志级别的映射
from config import CONF

Log_DICT = {
	'debug': logging.DEBUG,
	'info': logging.INFO,
	'warning': logging.WARNING,
	'error': logging.ERROR
}


# 创建一个logger工具类
class LogUtil:
	# 输出文件名称，日志名称，日志级别
	def __init__(self, log_file, log_name, log_level):
		self.log_file = log_file
		self.log_name = log_name
		self.log_level = log_level

		# 1、创建一个logger对象
		self.logger = logging.getLogger(self.log_name)
		# 2、设置logger的日志级别
		self.logger.setLevel(Log_DICT[log_level])
		# 判断logger是否已存在handler，不存在才需要去创建
		if not self.logger.handlers:
			# 3、创建 控制台handler 和 文件handler
			console_hanler = logging.StreamHandler()
			file_handler = logging.FileHandler(self.log_file)
			# 4、定义 控制台handler 和 文件handler 日志级别
			console_hanler.setLevel(Log_DICT[log_level])
			file_handler.setLevel(Log_DICT[log_level])
			# 5、定义日志输出格式
			formatter = logging.Formatter(
				'%(asctime)s   %(name)s  %(levelname)s  %(filename)s  [line:%(lineno)d]  %(message)s')
			# 6、设置 控制台handler 和 文件handler 日志显示格式
			console_hanler.setFormatter(formatter)
			file_handler.setFormatter(formatter)
			# 7、添加  控制台handler 和 文件handler
			self.logger.addHandler(console_hanler)
			self.logger.addHandler(file_handler)


# 日志工具类的使用：初始化参数数据
# 日志文件名称、日志文件级别
# 日志文件名称=logs目录 + 当前时间戳 + 文件扩展名
# logs目录
logs_path = CONF.get_logs_path()
# 当前时间戳
current_time = datetime.datetime.now().strftime('%Y-%m-%d')
# 文件扩展名
log_extension = ConfigYaml().get_config_log_extention()
# 拼接文件
logfile = os.path.join(logs_path, current_time + log_extension)
print(logfile)
# 获取日志文件级别
loglevel = ConfigYaml().get_config_log_level()


# 2、对外方法，初始化LogUtil工具类，提供其它类使用
def my_log(log_name=__file__):
	return LogUtil(log_file=logfile, log_name=log_name, log_level=loglevel).logger


if __name__ == '__main__':
	my_log('小电机').debug('this is a debug 运行记录信息')

