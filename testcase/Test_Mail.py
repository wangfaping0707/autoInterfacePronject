import requests


# 定义登录方法
def login():
	url = "http://211.103.136.242:8064/authorizations/"
	data = {"username": "python", "password": "12345678"}
	# 发送post请求
	res = requests.post(url=url, json=data)
	print(res.json())


if __name__ == '__main__':
	login()
