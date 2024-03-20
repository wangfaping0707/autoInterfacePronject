def Login(user, passwd):
	"""
	登录方法，用户名和密码是字符串类型，同时用户名长度至少要4位，密码长度至少6位
	:param user: 用户名
	:param password: 登录密码
	:return: 字符串  登录结果
	"""
	user_info = {"user": "jianshen", "passwd": "12345678"}
	if not isinstance(user, str) or not isinstance(passwd, str):
		return "用户名或密码类型不正确"
	elif len(user) < 4:
		return "用户名长度小于4"
	elif len(passwd) < 6:
		return "密码长度小于6"
	elif user_info['user'] != 'jianshen' or user_info['passwd'] != '12345678':
		return "用户名或密码错误"
	else:
		return "恭喜,登录成功！"
