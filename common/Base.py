"""
TypeError: object supporting the buffer API required  https://blog.csdn.net/weixin_44809381/article/details/122804773
pycharm 使用 Pymysql 链接数据库报错 TypeError: object supporting the buffer API required
原因：是因为 password 需要 str 格式字符串 而我写成了int类型
把 password 改成字符串 str 格式即可
"""

# 初始化---数据库对象
from config.CONF import ConfigYaml
from utils.MysqlUtil import Mysql
from utils.LogUtil import my_log
import subprocess
from utils.EmailUtil import SendEmail


# 定义初始化数据库对象方法
def init_db(db_alias):
	"""
	获取 数据库登录所需要的信息+ 新建数据库链接对象
	:param db_alias:
	:return:
	"""
	db_info = ConfigYaml().get_db_config_info(db_alias)
	host = db_info["db_host"]
	user = db_info["db_user"]
	passwd = db_info["db_passwd"]
	db_name = db_info["db_name"]
	charset = db_info["db_charset"]
	port = int(db_info["db_port"])
	# 新建数据库链接对象
	db_conn = Mysql(host, user, passwd, db_name, charset, port)
	print(db_conn)
	return db_conn


# 自动生成allure报告
# def allure_report():
# 	# 生成报告的命令
# 	allure_cmd='allure generate outputs/allure_results_files -o outputs/html --clean'
# 	# 执行subprocess.call方法
# 	my_log().info("报告地址")
# 	try:
# 		subprocess.call(allure_cmd,shell=True)
# 	except Exception as f:
# 		print(f)
# 		my_log(.error('用例执行失败，请检查一下环境配置'))
# 		raise

def send_email(report_path_html='', content='', title='自动化测试练习'):
	email_info = ConfigYaml().get_email_info()
	smtp_addr = email_info['smtpserver']
	username = email_info['username']
	password = email_info['password']
	recv = email_info['receiver']
	email_obj = SendEmail(
		smtp_addr=smtp_addr,
		username=username,
		password=password,
		recv=recv,
		title=title,
		content=content,
		file=report_path_html
	)


if __name__ == '__main__':
	init_db("db_1")
	send_email()
