# 使用热加载的类,替换请求参数中的类
# 单接口测试使用
import json
from utils.YamlUtil import YamlReader
import re
from utils.debugtalk import DebugTalk
import json
from utils.configparserUtil import ConfigparserReader
from utils.RequestsUtil import SendRequests
import jsonpath
from utils.assertion_tools import Assertions
import allure
from utils.log_tool.log_tool import logger

class RequestsBase:

	def __init__(self):
		self.conf = ConfigparserReader(r'./data/config.ini')
		self.send_request = SendRequests()
		self.yaml_reader = YamlReader(r'./extract.yml')
		self.assertion = Assertions()

	def parse_and_replace_variables(self, yaml_data):
		"""
		解析并替换 yaml 数据中的变量引用，如：${get_extract_data('goodids', 3), 解析 热加载
		:param yaml_data: 被解析的yaml数据
		:return:
		"""
		yaml_data_str = None
		if isinstance(yaml_data, str):
			yaml_data_str = yaml_data
		else:
			yaml_data_str = json.dumps(yaml_data, ensure_ascii=False)
		# print(f'解析替换之前：{yaml_data_str}')
		# _ 在for循环中表示展位符，没有实际含义，后续代码也不会用到这个变量
		# print(f'yaml_data_str:{yaml_data_str}')
		for _ in range(yaml_data_str.count('${')):
			if '${' in yaml_data_str and '}' in yaml_data_str:
				# 获取要切片的开始和结束索引
				start_index = yaml_data_str.index('$')
				end_index = yaml_data_str.index('}', start_index)
				# 开始进行切片操作
				variable_data = yaml_data_str[start_index:end_index + 1]
				# print(f'切片获取的引用函数变量：{variable_data}')

				# 使用正则表达式提取 variable_data 变量中，函数的名称 和 对应的参数
				match = re.match(r'\$\{(\w+)\((.*?)\)\}', variable_data)
				# print(f'---正则匹配返回---：{match.groups()}')
				if match:
					# 字符串形式的：函数名 + 函数的参数
					func_name, func_params = match.groups()
					# 将获取到的函数参数进行分割操作
					if func_params:
						# print(f'func_params:{func_params}', type(func_params))
						func_params = func_params.split(',')
					# print(f'func_params:{func_params}', type(func_params))
					else:
						func_params = []
					# 利用获取的到函数名称和参数列表，使用面向对象的 反射来调用函数，获取到函数的执行结果
					extract_data = getattr(DebugTalk(), func_name)(*func_params)
					# print(f'提取到结果：{extract_data}')
					# 将原始字符串 yaml_data_str 中的 函数变量引用部分 替换为  反射---函数的执行结果
					# re.escape()函数:用于将一个字符串中的特殊字符转义成正则表达式中的普通字符
					yaml_data_str = re.sub(re.escape(variable_data), str(extract_data), yaml_data_str)
		# 还原数据，将其转换为字典类型：str====>dict
		# print(f'解析替换之后：{yaml_data_str}')
		try:
			data = json.loads(yaml_data_str)
		except json.JSONDecodeError:
			data = yaml_data_str
		return data

	@classmethod
	def allure_attach_dict_result(cls, result):
		"""
		传入如果是字典类型的数据，就将其转换为字符串类型，并做格式化处理
		:param response:
		:return:
		"""
		if isinstance(result, dict):
			allure_response = json.dumps(result, ensure_ascii=False, indent=4)
		else:
			allure_response = result
		return allure_response

	def execute_test_cases(self, base_info, testcase):
		"""
		规范yaml接口信息，执行接口，提取结果以及断言操作
		:param base_info: 参数类型；dict  yaml文件里面接口基本信息
		:param testcase: 参数类型；dict  yaml文件里面接口测试用例信息
		"""
		print(f'初始入参base_info：{base_info}')
		print(f'初始入参testcase：{testcase}')
		try:
			# 从 base_info提取 请求接口的四要素：请求地址、请求方法、请求参数、请求头、出参等
			# 获取ip地址
			conf_host = self.conf.get_Host_conf('host')
			# 拼接接口请求url
			url = conf_host + base_info['url']
			allure.attach(body=url, name='接口地址', attachment_type=allure.attachment_type.TEXT)
			# 获取接口名称
			api_name = base_info['api_name']
			allure.attach(body=api_name, name='接口名称', attachment_type=allure.attachment_type.TEXT)
			# 获取请求方法
			method = base_info['method']
			allure.attach(body=method, name='请求方法', attachment_type=allure.attachment_type.TEXT)
			# 获取请求头：请求头是可选字段，因此值是可变的，所以可能有热加载
			headers = base_info.get('headers', None)
			if headers is not None:
				if isinstance(headers, str):  # 是 字符串类型---说明需要使用热加载进行解析了，类似于这种 ${get_headers(data)}
					headers = eval(self.parse_and_replace_variables(headers))
				else:
					headers = headers
			# body的类型只能是字符串类型，所以需要做转化操作
			allure.attach(body=json.dumps(headers), name='请求头', attachment_type=allure.attachment_type.JSON)
			# 获取cookie值,请求头是可选字段，因此值是可变的，所以可能用到热加载
			cookie = base_info.get('cookies')
			if cookie is not None:
				if isinstance(cookie, str):
					# 此处eval将字符串形式的字典  转换为 字典
					cookie = eval(self.parse_and_replace_variables(cookie))
				else:
					cookie = cookie
			allure.attach(body=json.dumps(cookie), name='cookie', attachment_type=allure.attachment_type.JSON)

			# 提取测试用例testcase里面的字段信息
			# 测试用例名称
			case_name = testcase.pop('case', None)
			allure.attach(body=case_name,name='测试用例名称',attachment_type=allure.attachment_type.TEXT)

			print(f'断言替换之前，validation:{testcase.get("validation")}')
			# 提取用例的断言结果
			# 如果login.yml中 断言结果需要调用别的函数或者读取中间文件获取，则需要使用到热加载,contain:{'msg':'${get_extract_data(login_status)}'}
			val_result = self.parse_and_replace_variables(testcase.get('validation'))
			testcase['validation'] = val_result
			validation = testcase.pop('validation')
			print(f'断言替换之后，validation:{validation}', type(validation))

			print('************分割线*************')
			# 处理接口返回值提取部分
			extract = testcase.pop('extract', None)
			extract_list = testcase.pop('extract_list', None)

			# 处理文件上传
			# files = testcase.pop('files', None)
			# if files:
			# 	for fk, fv in files.items():
			# 		files = {fk: open(fv, mode='rb')}

			# 查看处理后，只剩下请求参数了
			print(f'处理前testcase：{testcase}')
			# 如果请求参数中某个请求参数的值是动态变化，则需要用到热加载, 热加载的函数需要在debugtalk.py文件中
			for param_type, param_value in testcase.items():
				allure.attach(body=param_type, name='参数类型', attachment_type=allure.attachment_type.TEXT)
				if param_type in ['params', 'data', 'json']:
					request_val = self.parse_and_replace_variables(param_value)
					testcase[param_type] = request_val
					# 在allure报告中打印出请求参数
					allure.attach(self.allure_attach_dict_result(request_val), '请求参数', allure.attachment_type.JSON)
			print(f'处理后testcase：{testcase}', type(testcase))

			# testCase中可能不止一个case，所以需要在循环中，发起请求
			response = self.send_request.execute_api_request(api_name=api_name, url=url, method=method,
			                                                 headers=headers, case_name=case_name, cookies=cookie,
			                                                 **testcase)
			# 获取响应状态码 和 响应文本信息
			status_code, response_text = response.status_code, response.text
			logger.info(f'接口实际返回结果：{response_text}')
			# 在allure报告中显示接口实际返回来的响应信息
			allure.attach(body=self.allure_attach_dict_result(response.json()), name='接口实际响应信息',
			              attachment_type=allure.attachment_type.JSON)

			# 请求参数yaml文件中如果有extract字段，则表明接口请求成功之后，需要提取一些返回的字段值，并写入到extract.yml文件中，供后续接口取用
			if extract is not None:
				self.extract_data(extract, response.text)
			# 请求参数yaml文件中如果有extract_list字段，则表明接口请求成功之后，需要提取一些返回的字段值，并写入到extract.yml文件中，供后续接口取用
			if extract_list is not None:
				self.extract_data_list(extract_list, response.text)

			# 处理接口断言
			self.assertion.assert_result(validation, response.json(), status_code)
		except Exception as e:
			logger.error(f'接口调用出现异常，请检查')
			raise e

	def extract_data(self, testcase_extract, response_text):
		"""
		提取接口返回的单个字段值，并写入到中间文件中； 支持正则表达式 + json提取器 进行值的提取
		:param testcase_extract: dict类型，yaml文件中的extract值，如{'token':$.token}
		:param response_text: (str)接口的实际返回值
		:return:
		"""
		print(testcase_extract)
		extract_data = None
		try:
			for key, value in testcase_extract.items():
				# 判断value是否是 正则表达式，如果是，则使用正则表达式来取值，如：value是否为类似于这样的数值 {'token': '$.token'}
				if any(pat in value for pat in ['(.*?)', '(.+?)', r'(\d+)', r'(\d*)']):
					# 正则表达式来取值
					ext_list = re.search(value, response_text)
					if r'(\d+)' in value:
						# 将提取的值组合成为一个字典
						extract_data = {key: int(ext_list.group(1))}
					else:
						extract_data = {key: ext_list.group(1)}
				elif '$' in value:
					# 使用jsonpath进行值的提取
					extract_json = jsonpath.jsonpath(json.loads(response_text), value)[0]
					# 判断值是否被 提取到，然后进行值的组合
					if extract_json:
						extract_data = {key: extract_json}
					else:
						# extract_data = {key: 'jsonpath未提取到值，请检查接口返回信息或表达式'}
						print('jsonpath未提取到值，请检查接口返回信息或表达式。。。。。')
				# 将提取的值写入到中间文件extract.yml文件中
				if extract_data:
					self.yaml_reader.write_extract_yaml(extract_data)
		except Exception as e:
			raise e

	def extract_data_list(self, testcase_extract_list, response_text):
		"""
		提取接口返回的多个字段值，并写入到中间文件中； 支持正则表达式 + json提取器 进行值的提取
		:param testcase_extract_list: dict类型，yaml文件中的 extract_list 值，如{'token':$.token}
		:param response_text: (str)接口的实际返回值
		:return:
		"""
		extract_data = None
		try:
			for key, value in testcase_extract_list.items():
				# 判断value是否是 正则表达式，如果是，则使用正则表达式来取值，如：value是否为类似于这样的数值 {'token': '$.token'}
				if any(pat in value for pat in ['(.*?)', '(.+?)', r'(\d+)', r'(\d*)']):
					# 正则表达式来取值
					ext_list = re.findall(value, response_text, re.S)
					# 将提取的值组合成为一个字典
					if ext_list:
						extract_data = {key: ext_list}
					else:
						print('正则表达式没有提取到对应的值，请检查。。。。')
				elif '$' in value:
					extract_json = jsonpath.jsonpath(json.loads(response_text), value)
					if extract_json:
						extract_data = {key: extract_json}
					else:
						print('jsonpath表达式没有提取到对应的值，请检查。。。。')
				# 将提取的值写入到中间文件extract.yml文件中
				if extract_data:
					self.yaml_reader.write_extract_yaml(extract_data)

		except Exception as e:
			raise e


if __name__ == '__main__':
	# s1 = YamlReader(r'../data/adduser.yml')
	# datas = s1.read_yaml()[0]
	# print(datas, type(datas))
	# r1 = RequestsBase().parse_and_replace_variables(datas)
	# print(r1)
	print('***********************************************************************************************************')
	s2 = YamlReader(r'../data/login.yml')
	api_info = s2.read_yaml()[0]
	print(api_info)
	r2 = RequestsBase().execute_test_cases(api_info)
