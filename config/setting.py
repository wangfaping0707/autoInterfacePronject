import os
import sys

# 项目的根路径
PROJECT_BASE_PATH = os.path.dirname(os.path.dirname(__file__))
sys.path.append(PROJECT_BASE_PATH)
# 日志文件夹路径
log_path = os.path.join(PROJECT_BASE_PATH, 'logs')
# print(log_path)

# 钉钉机器人签名和地址
secret = 'SECb163daa45904540212492d8ad7bf7c3ce428fae5211c2e94b1f0926be0778181'
webhook = 'https://oapi.dingtalk.com/rebot/send?access_token=df849617e1f9593fd9c\
           31f75ce4fdf2fea8fec39c7b714a65f20413444f5cea5'

# 设置是否发送钉钉群消息，默认为False，不会发送群消息
is_dd_msg = True
