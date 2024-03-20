# 以后导包直接导入下面这种,logging其实是包名，非模块名

import logging.handlers

# 获取日志器
logger = logging.getLogger("找工作-日志器")

# 设置获取日志的级别
logger.setLevel(logging.INFO)

# 设置日志文件处理器：根据时间来切割文件

trfh = logging.handlers.TimedRotatingFileHandler(filename='./time.log', when='M', interval=1, backupCount=3, encoding='utf-8')

# 格式器：字符串形式
fmt_style = '%(asctime)s   %(name)s  %(levelname)s  %(filename)s  [line:%(lineno)d]  %(message)s'

# 创建格式器
fm = logging.Formatter(fmt=fmt_style)

# 给处理器添加 日志格式器
trfh.setFormatter(fmt=fm)

# 将日志处理器添加到logger中
logger.addHandler(trfh)

# 输入打印的日志信息
logger.debug('debug..........')
logger.info('info-----------------------')
logger.warning('warning-持续警告中----')
