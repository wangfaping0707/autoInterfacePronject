import os
import sys
from config.setting import log_path
import time
# from logging.handlers import RotatingFileHandler    #按日志文件大小进行切割，滚动备份日志文件
import logging.handlers
import colorlog  # 这个模块可以控制不同级别的日志显示不同的颜色

# 日志文件夹路径
logs_path = log_path

if not os.path.exists(logs_path):
	os.mkdir(logs_path)

# 日志文件夹路径 + 日子名称
logfile_name = os.path.join(logs_path, 'test_{}.log'.format(time.strftime('%Y-%m-%d')))
print(logfile_name)


class LogTool:
	# 日志类使用单例模式，避免日志重复打印
	logger = None

	@classmethod
	def setting_log_color(cls):
		""" 控制不同级别的日志显示不同的格式"""
		log_color_config = {
			'DEBUG': 'cyan',
			'INFO': 'green',
			'ERROR': 'red',
			'WARNING': 'yellow',
			'CRITICAL': 'red'
		}
		style = '%(log_color)s  %(asctime)s   %(name)s  %(levelname)s  %(filename)s  [line:%(lineno)d]  [%(module)s:%(funcName)s]  %(message)s'
		# 创建日志显示格式器
		color_format = colorlog.ColoredFormatter(fmt=style, log_colors=log_color_config)
		return color_format

	@classmethod
	def get_logger(cls):
		if cls.logger is None:
			# 创建日志器
			cls.logger = logging.getLogger(__name__)

			# 设置日志器接受日志级别
			cls.logger.setLevel(logging.DEBUG)

			# 设置日志显示格式样式
			style = '%(asctime)s  %(name)s  %(levelname)s  %(filename)s  [line:%(lineno)d]  [%(module)s:%(funcName)s]  %(message)s'
			# 日志样式格式器
			log_format = logging.Formatter(fmt=style)

			# 依据不同日志等级，显示不同的颜色
			stream_format = cls.setting_log_color()

			# 设置日志控制台处理器
			console_handler = logging.StreamHandler()
			console_handler.setLevel(logging.DEBUG)
			console_handler.setFormatter(stream_format)
			cls.logger.addHandler(console_handler)

			# 设置日志写入文件处理器: 按日志文件大小进行切割，滚动备份日志文件
			file_handler = logging.handlers.RotatingFileHandler(filename=logfile_name, mode='a+', maxBytes=5242880,
			                                                    backupCount=5, encoding='utf-8')
			file_handler.setLevel(logging.DEBUG)
			file_handler.setFormatter(log_format)
			cls.logger.addHandler(file_handler)
		return cls.logger

logger = LogTool.get_logger()
# if __name__ == '__main__':
# 	logger = LogTool.get_logger()
# 	logger.debug('debug日志输出。。。。。')
# 	logger.info('info日志输出。。。。。。')
# 	logger.error('error日志输出。。。。。。')
# 	logger.warning('warning日志输出。。。。。。')
# 	logger.critical('critical日志输出。。。。。。')
