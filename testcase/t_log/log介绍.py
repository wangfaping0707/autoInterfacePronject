"""
原文链接：https://blog.csdn.net/fullbug/article/details/129648873
https://zhuanlan.zhihu.com/p/476549020?utm_id=0

Python的logging库采用模块化方法，并提供了几类组件：记录器，处理程序，过滤器和格式化程序。

记录器（Logger）：提供应用程序代码直接使用的接口。
处理器（Handler）：将日志记录（由记录器创建）发送到适当的目的地。
筛选器（Filter）：提供了更细粒度的功能，用于确定要输出的日志记录。
格式器（Formatter）：程序在最终输出日志记录的内容格式。

logging的工作流程：以记录器Logger为对象，设置合适的处理器Handler，辅助以筛选器Filter、格式器Formatter，设置日志级别以及常用的方法，最终输出理想的日志记录给到指定目标
一个Logger可以包含多个Handler；
每个Handler可以设置自己的Filter和Formatter；

设置日志输出格式：
"%(asctime)s - %(levelname)s %(name)s %(filename)s [line:%(lineno)d] - %(message)s"

asctime：%(asctime)s 日志发生时间 表示 LogRecord 何时被创建的，供人查看时间值。 默认形式为 ‘2003-07-08 16:49:45,896’ （逗号之后的数字为时间的毫秒部分）。

levelname：%(levelname)s 日志级别  消息文本记录级别（‘DEBUG’，‘INFO’，‘WARNING’，‘ERROR’，‘CRITICAL’）

name: %(name)s logger实例名称  用于记录调用的日志记录器名称

filename: %(filename)s  日志发生的文件名  pathname 的文件名部分

[line:%(lineno)d]   日志发生所在的行  lineno %(lineno)d 发出日志记录调用所在的源行号（如果可用）,[line:] 这是一种人为写的格式

message：%(message)s  日志消息内容  记入日志的消息，即 msg % args 的结果。 这是在发起调用 Formatter.format() 时设置的


getLogger() 返回对具有指定名称的Logger实例的引用（如果提供了），或者如果没有指定，则返回对根实例的引用。
这些名称是以句点分隔的层次结构。使用相同名称多次调用getLogger（）将返回对同一记录器对象的引用。
在层级列表中较低的记录器是列表中较高记录器的子级。例如，给定一个名为foo的Logger, 那么，foo.bar, foo.bar.baz, and foo.bam 皆是foo的后代
logger = logging.getlogger()   logger 对根实例的引用  名称为root
logger = logging.getLogger('小电机')   定名称的Logger实例的引用 名称为 小电机


"""