"""
https://blog.csdn.net/GitHub_miao/article/details/136900171

Python configparser模块详解：配置文件管理利器

Python中有许多用于处理配置文件的模块，其中configparser模块是一种简单而强大的工具，用于读取和写入INI格式的配置文件。
本文将深入介绍configparser模块的各种用法，并提供丰富的示例代码。

什么是configparser模块？
configparser模块是Python标准库中的一部分，用于处理INI格式的配置文件。它提供了简单而直观的接口，使得读取和写入配置信息变得轻松且易于维护。

安装和导入configparser模块
configparser模块是Python标准库的一部分，因此无需额外安装。

只需要在代码中导入它即可：
import configparser

配置文件的基本结构
INI格式的配置文件由多个节（section）和每个节下面的多个选项（option）组成。每个选项都有对应的值，可以是字符串、整数、布尔值等。

示例配置文件（config.ini）：
[Database]
host = localhost
port = 5432
username = admin
password = password123

[Logging]
level = INFO
file = app.log

读取配置文件:
使用configparser模块可以轻松地读取配置文件中的信息。
可以通过节名和选项名来获取对应的值：
"""
from configparser import ConfigParser

# 创建 配置解析器对象
cfg = ConfigParser()

# 预定义一个配置文件路径
config_file = 'config_info.ini'

# 读取配置文件
cfg.read(config_file)

# 获取指定的section的option值
v1 = cfg.get('Database', 'host')
print(v1)
# 读取数据库配置信息
db_host = cfg['Database']['host']
db_port = cfg['Database'].getint('port')
db_username = cfg['Database']['username']
db_password = cfg['Database']['password']

# 读取日志配置信息
log_level = cfg['Logging']['level']
log_file = cfg['Logging']['file']
print(log_file)

print('-----------------------------------------------------------')
# 添加新的节和选项
cfg.add_section('Color')
cfg.set('Color', 'c1', 'blue')

# 写入配置信息到文件
with open('new_config.ini', 'w') as configfile:
    cfg.write(configfile)


# 添加新的节和选项
cfg.add_section('Hobby')
cfg.set('Hobby', 's1', 'swim')
with open(config_file, 'w') as f:
    cfg.write(f)