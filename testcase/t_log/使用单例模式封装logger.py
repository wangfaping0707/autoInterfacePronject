import logging.handlers


class GetLogger:
	logger = None

	@classmethod
	def get_logger(cls):
		if cls.logger is None:
			# 创建日志器
			cls.logger = logging.getLogger("电动小马达")

			# 设置日志器接受日志级别
			cls.logger.setLevel(logging.INFO)

			# 设置写入文件处理器
			file_handler = logging.handlers.TimedRotatingFileHandler(filename='./content.log', when='midnight',
			                                                         interval=1,
			                                                         backupCount=10, encoding="utf-8")
			# 创建控制台处理器
			console_handler = logging.StreamHandler()

			# 设置日志显示格式样式
			style = '%(asctime)s   %(name)s  %(levelname)s  %(filename)s  [line:%(lineno)d]  %(message)s'

			# 创建格式器
			fm = logging.Formatter(fmt=style)

			# 将格式器分别添加到控制台处理器 和 文件处理器
			console_handler.setFormatter(fmt=fm)
			file_handler.setFormatter(fmt=fm)

			# 将处理器添加到日志器中
			cls.logger.addHandler(console_handler)
			cls.logger.addHandler(file_handler)
		return cls.logger

if __name__ == '__main__':
    logger = GetLogger.get_logger()
    logger.info('hello,你好啊。。。')