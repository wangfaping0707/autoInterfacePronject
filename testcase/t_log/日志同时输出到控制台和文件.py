import logging

# 1、创建一个logger对象
logger = logging.getLogger('小灰机来啦')
# 2、设置logger的日志级别
logger.setLevel(logging.DEBUG)
# 3、创建 控制台handler 和 文件handler
console_hanler = logging.StreamHandler()
file_handler = logging.FileHandler('./file.log')
# 4、定义 控制台handler 和 文件handler 日志级别
console_hanler.setLevel(logging.DEBUG)
file_handler.setLevel(logging.INFO)
# 5、定义日志输出格式
formatter = logging.Formatter('%(asctime)s   %(name)s  %(levelname)s  %(filename)s  [line:%(lineno)d]  %(message)s')
# 6、设置 控制台handler 和 文件handler 日志显示格式
console_hanler.setFormatter(formatter)
file_handler.setFormatter(formatter)
# 7、添加  控制台handler 和 文件handler
logger.addHandler(console_hanler)
logger.addHandler(file_handler)
# 8、运行输出
logger.debug('this is a debug message')
logger.info('this is a info message')
logger.warning('this is a FBI warning')
