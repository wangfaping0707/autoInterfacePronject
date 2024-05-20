from utils.exception_utils.exceptions import AssertTypeError
import jsonpath
import operator
from utils.db_connector.connectMysql import ConnectMysql
import allure
import json
from utils.log_tool.log_tool import logger


class Assertions:
	"""
	接口断言模式封装
	1)、响应状态码断言
	2)、包含模式断言
	3)、相等断言
	4)、不相等断言
	5)、数据断言断言
	"""

	@classmethod
	def assert_statue_code(cls, expected_code, actual_code):
		"""
		接口响应的状态码断言
		:param actual_code: 接口实际返回的状态码
		:param expected_code: yaml文件中定义的预期返回状态码
		:return: 为True 或 False
		"""
		# flag 断言结果标识，flag = 0 表示断言成功，flag !=0 表示断言失败
		flag = 0
		if int(expected_code) == int(actual_code):
			logger.info(f'状态码断言成功：接口实际返回状态码{expected_code} == {actual_code}')
			allure.attach(body=f'预期结果：{str(expected_code)}\n实际结果：{str(actual_code)}', name='状态码断言：成功',
			              attachment_type=allure.attachment_type.TEXT)
			return flag
		else:
			logger.error(f'状态码断言失败：接口实际返回状态码{expected_code} != {actual_code}')
			allure.attach(body=f'预期结果：{str(expected_code)}\n实际结果：{str(actual_code)}', name='状态码断言：失败',
			              attachment_type=allure.attachment_type.TEXT)
			flag += 1
			return flag

	@classmethod
	def assert_contain(cls, expected_result, response):
		"""
		字符串包含模式：断言预期结果字符串是否包含在接口实际响应返回信息中
		:param expected_result: 参数类型是字典，（dict）yaml文件中contain模式的数据，类似于这种：{'msg': '登录成功'}
		:param response: （dict）接口实际响应信息
		:return:
		"""
		# flag 断言结果标识，flag = 0 表示断言成功，flag !=0 表示断言失败
		flag = 0
		for assert_key, assert_value in expected_result.items():
			# 提取实际接口响应信息中，assert_key 字段的值 然后与预期值 assert_value进行比对
			response_list = jsonpath.jsonpath(response, f'$..{assert_key}')
			if response_list and isinstance(response_list[0], str):
				response_str = ''.join(response_list)

				success_message = f'包含模式断言成功：预期结果【{assert_value}】存在于实际结果【{response_str}】中'
				failure_message = f'包含模式断言失败：预期结果【{assert_value}】不存在于实际结果【{response_str}】中'
				if assert_value in response_str:
					logger.info(success_message)
				else:
					logger.error(failure_message)
					flag += 1
		return flag

	@classmethod
	def assert_equal(cls, expected_result, response):
		"""
		相等断言：根据yaml里面的validation关键字下面的eq模式数据 去跟接口实际响应信息比对
		:param expected_result: （dict） yaml文件里面的eq值
		:param response: （dict）接口实际响应结果
		:return:
		"""
		# flag 断言结果标识，flag = 0 表示断言成功，flag !=0 表示断言失败
		flag = 0
		# 先判断期望值和接口实际响应值是不是字典类型
		print(f'expected_result:{expected_result}')
		print(f'response:{response}')
		if isinstance(expected_result, dict) and isinstance(response, dict):
			# 找到预期结果和实际结果共同的key
			common_key = list(expected_result.keys() & response.keys())
			# 判断common_key是否不为空
			if common_key:
				for key in common_key:
					# 根据相同的key分别去 预期结果 和 实际结果中去取key对应的值，然后组成两个新的字典进行比对
					new_expected_dic = {key: expected_result[key]}
					new_response_dic = {key: response[key]}
					eq_assert = operator.eq(new_expected_dic, new_response_dic)
					if eq_assert:
						logger.info(f'相等断言成功：接口预期结果{new_expected_dic} == 接口返回实际结果{new_response_dic}')
						allure.attach(body=f'预期结果{json.dumps(new_expected_dic)}\n实际结果{json.dumps(new_response_dic)}',
						              name='相等断言：成功',
						              attachment_type=allure.attachment_type.JSON)
					else:
						flag += 1
						logger.error(f'相等断言失败：接口预期结果{new_expected_dic} ！= 接口返回实际结果{new_response_dic}')
						allure.attach(body=f'预期结果{json.dumps(new_expected_dic)}\n实际结果{json.dumps(new_response_dic)}',
						              name='相等断言：失败',
						              attachment_type=allure.attachment_type.JSON)
			else:
				flag += 1
				logger.error('相等断言失败，请检查yaml文件eq模式的预期结果或接口返回值是否正确')

		return flag

	@classmethod
	def assert_not_equal(cls, expected_result, response):
		"""
		不相等断言：根据yaml里面的validation关键字下面的 ne 模式数据 去跟接口实际响应信息比对
		:param expected_result: （dict） yaml文件里面的ne值
		:param response: （dict）接口实际响应结果
		:return:
		"""
		# flag 断言结果标识，flag = 0 表示断言成功，flag !=0 表示断言失败
		flag = 0
		# 先判断期望值和接口实际响应值是不是字典类型
		print(f'expected_result:{expected_result}')
		print(f'response:{response}')
		if isinstance(expected_result, dict) and isinstance(response, dict):
			# 找到预期结果和实际结果共同的key
			common_key = list(expected_result.keys() & response.keys())
			# 判断common_key是否不为空
			if common_key:
				for key in common_key:
					# 根据相同的key分别去 预期结果 和 实际结果中去取key对应的值，然后组成两个新的字典进行比对
					new_expected_dic = {key: expected_result[key]}
					new_response_dic = {key: response[key]}
					eq_assert = operator.ne(new_expected_dic, new_response_dic)
					if eq_assert:
						logger.info(f'不相等断言成功：接口预期结果{new_expected_dic} ！= 接口返回实际结果{new_response_dic}')
					else:
						flag += 1
						logger.error(f'不相等断言失败：接口预期结果{new_expected_dic} == 接口返回实际结果{new_response_dic}')
			else:
				flag += 1
				logger.error('相等断言失败，请检查yaml文件eq模式的预期结果或接口返回值是否正确')

		return flag

	@classmethod
	def assert_database(cls, expected_result):
		"""
		数据库断言
		:param expected_result: （dict） yaml文件里面的db值   {'code': 200}
		:return:
		"""
		# flag 断言结果标识，flag = 0 表示断言成功，flag !=0 表示断言失败
		flag = 0
		cm = ConnectMysql()
		db_value = cm.query(expected_result)
		if db_value:
			logger.info('数据库断言成功')
		else:
			flag += 1
			logger.error('数据库断言失败')
		return flag

	@classmethod
	def assert_result(cls, expected_result, response, status_code):
		"""
		断言主函数：通过 all_flag标记：如果all_flag=0,表示断言成功，all_flag !=0 表示断言失败
		:param response: 请求接口之后，实际返回的响应信息
		:param expected_result: yaml文件中 validation 关键词下面的 预期结果 ,类型是列表list validation:[{'code': 200}, {'contain': {'msg': '登录成功'}}, {'eq': {'msg': '登录成功'}}]
		:param status_code: 接口的实际响应状态码
		:return:
		"""
		all_flag = 0
		# 定义个断言函数字典
		assert_methods = {
			'code': cls.assert_statue_code,
			'contain': cls.assert_contain,
			'eq': cls.assert_equal,
			'ne': cls.assert_not_equal,
			'db': cls.assert_database
		}
		try:
			print(f'expected_result:{expected_result}')
			# 迭代循环列表，取出其中的字典 [{'code': 200}, {'contain': {'msg': '登录成功'}}, {'eq': {'msg': '登录成功'}}]
			for dic in expected_result:
				# 迭代循环字典  assert_value 期望结果
				for assert_type, assert_value in dic.items():
					# 根据字段assert_type 从assert_methods字典取出对应的断言函数
					assert_method = assert_methods.get(assert_type)
					if assert_method:
						# 调用对应的断言函数，并传入适当的参数
						if assert_type == 'code':
							flag = assert_method(assert_value, status_code)
						elif assert_type in ['contain', 'eq', 'ne']:
							flag = assert_method(assert_value, response)
						elif assert_type == 'db':
							flag = assert_method(assert_value)

						all_flag += flag
					else:
						# f'不支持{assert_type}这种断言模式'
						raise AssertTypeError(f'不支持{assert_type}这种断言模式')
		except Exception as e:
			raise e
		assert all_flag == 0, '接口测试失败'
		logger.info('接口测试成功')


if __name__ == '__main__':
	validation = [{'code': 200}, {'contain': {'msg': '登录成功'}}, {'eq': {'msg': '登录成功'}}]
	# 预期结果
	d1 = [{'code': 200}, {'contain': {'msg': '登录成功', 'color': 'red'}}, {'eq': {'red_flag': '革命进行中', 'sex': 'female'}},
	      {'ne': {'blue_flag': '苹果', 'size': 20}}]
	# 调用接口返回的实际结果
	d2 = {'msg': '登录成功', 'color': 'red', 'red_flag': '革命进行中', 'sex': 'female', 'blue_flag': '苹果1', 'size': 201}
	# Assertions.assert_statue_code(200,200)
	# Assertions.assert_contain(d1, d2)
	Assertions.assert_result(d1, d2, 200)
