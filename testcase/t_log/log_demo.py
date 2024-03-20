"""
1、导入logging包
2、设置配置信息
3、定义日志名称getLogger
4、info、debug
"""
import logging

LOG_FORMATE = '%(asctime)s   %(name)s  %(levelname)s  %(filename)s  [line:%(lineno)d]  %(message)s'
# 配置日志输出级别及格式
logging.basicConfig(filename='testlog.log', filemode='w', level=logging.INFO, format=LOG_FORMATE)


# 创建一个logger
logger = logging.getLogger('小电机')
# logger.info()函数的意思是向日志系统输出一条info级别的日志记录

logging.info('hahhahh')
logger.info('info.......')
logger.debug('Debug......')
