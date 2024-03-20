import logging

# 日志信息输出到控制台

# 1、创建一个logger对象
logger = logging.getLogger('拖拉机')
# 2、设置log级别
logger.setLevel(logging.INFO)
# 3、创建StreamHandler
csh = logging.StreamHandler()
# 4、设置日志级别
csh.setLevel(logging.DEBUG)
# 5、定义日志输出格式
formatter = logging.Formatter('%(asctime)s   %(name)s  %(levelname)s  %(filename)s  [line:%(lineno)d]  %(message)s')
csh.setFormatter(formatter)
# 6、添加handler
logger.addHandler(csh)
# 7、运行输出
logger.debug('this is a debug message')
logger.info('this is a info message')