from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


class SendEmail:
	def __init__(self, smtp_addr, username, password, recv, title, content=None, file=None):
		self.smtp_addr = smtp_addr
		self.username = username
		self.password = password
		self.recv = recv
		self.title = title
		self.content = content
		self.file = file

	# 发送邮件方法
	def send_email(self):
		msg = MIMEMultipart()
		# 初始化邮件信息
		msg.attach(MIMEText(self.content, _charset='utf-8'))
		msg['Subject'] = self.title
		msg['From'] = self.username
		msg['To'] = self.recv
		# 判断邮件是否有附件
		if self.file:
			# MIMEText读取文件
			att = MIMEText(open(self.file).read())
			# 设置内容类型
			att['Content-Type'] = 'application/octet-stream'
			# 设置附件头
			att['Content-Disposition'] = 'attachment;filename="%s' % self.name
			# 将内容附加到邮件主体
			msg.attach(att)
		# 登录邮件服务器
		self.smtp = smtplib.SMTP(host=self.smtp_addr, port=25)
		self.smtp.login(user=self.username, password=self.password)
		# 发送邮件
		self.smtp.sendmail(from_addr=self.username, to_addrs=self.recv, msg=msg.as_string())


if __name__ == '__main__':
	from config.CONF import ConfigYaml

	email_info = ConfigYaml().get_email_info()
	smtp_addr = email_info['smtpserver']
	username = email_info['username']
	password = email_info['password']
	recv = email_info['receiver']
	email_obj = SendEmail(smtp_addr, username, password, recv, '自动化测试练习')
