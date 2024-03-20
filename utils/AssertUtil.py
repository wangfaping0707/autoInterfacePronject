import json

from utils.LogUtil import my_log


# 1、定义封装类
class AssertUtil:
	# 2、初始化数据，日志
	def __init__(self):
		self.log = my_log('AssertUtil')

	# 验证code相等
	def assert_code(self, code, expected_code):
		"""
		验证返回状态码和期望状态码是否相等
		:param code:
		:param expected_code:
		:return:
		"""
		try:
			assert int(code) == int(expected_code)
			return '代码执行通过'
		except Exception as e:
			self.log.error(f'响应码错误，预期返回状态码{code},实际返回状态码{expected_code}')
			raise e

	# 验证body相等
	def assert_body(self, body, expected_body):
		"""
		验证返回body和期望body是否相等
		:param body:
		:param expected_body:
		:return:
		"""
		try:
			assert int(body) == int(expected_body)
			return '代码执行通过'
		except Exception as e:
			self.log.error(f'响应码错误，预期返回状态码{body},实际返回状态码{expected_body}')
			raise e

	# 验证bod包含
	def assert_body(self, body, expected_body):
		"""
		验证返回结果是否包含 期望结果
		:param body:
		:param expected_body:
		:return:
		"""
		try:
			body = json.dump(body)
			assert expected_body in body
			return 'body已包含'
		except Exception as e:
			self.log.error(f'不包含或body体转换json格式报错，预期返回状态码{body},实际返回状态码{expected_body}')
			raise e

