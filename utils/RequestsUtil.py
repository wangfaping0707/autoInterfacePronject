import requests
import json


# 两种封装请求类
# 方式一：
class Requests:
	def requests_api(self, url, data=None, json=None, headers=None, cookies=None, method='get'):
		'''增加方法的参数，根据method参数来判断请求方式'''
		if method == 'get':
			r = requests.get(url, data=data, cookies=cookies, json=json, headers=headers)
		elif method == 'post':
			r = requests.post(url, data=data, cookies=cookies, json=json, headers=headers)
		code = r.status_code
		try:
			body = r.json()
		except Exception as e:
			body = r.text
		# 将响应内容填充到字典
		res = dict()
		res['code'] = code
		res['body'] = body
		# 将字典返回
		return res

	# 重构get/post方法
	# 1、定义get方法
	def get(self, url, **kwargs):
		# 2、定义参数：url json headers cookies method
		# 3、调用公共方法
		return self.requests_api(url, method='get', **kwargs)

	# 2、定义post方法
	def post(self, url, **kwargs):
		return self.requests_api(url, method='post', **kwargs)



# 方式二

class RequestsUtil:
	# 类变量，通过类名访问，是session始终是同一个
	session = requests.session()

	# 统一请求封装,原理Connection:keep-alive保持活跃
	def send_request(self, method, url, data, **kwargs):
		# 将传进来的method全部转换为小写
		method = str(method).lower()
		# 判断请求方式
		if method == 'get':
			rep = RequestsUtil.session.request(method=method, url=url, params=data, **kwargs)
		else:
			# post请求使用str进行传参，所以需要将data转换为字符串形式，然后使用data=data
			data = json.dumps(data)
			rep = RequestsUtil.session.request(method=method, url=url, data=data, **kwargs)
		return rep.text
