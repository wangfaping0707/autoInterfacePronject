# 使用热加载的类,替换请求参数中的类
import json
from utils.YamlUtil import YamlReader
import re
from utils.debugtalk import DebugTalk
import json


class RequestsBase:

	def parse_and_replace_variables(self, yaml_data):
		"""
		解析并替换 yaml 数据中的变量引用，如：${get_extract_data('goodids', 3)
		:param yaml_data: 被解析的yaml数据
		:return:
		"""
		yaml_data_str = None
		if isinstance(yaml_data, str):
			print('德玛西亚')
			yaml_data_str = yaml_data
		else:
			yaml_data_str = json.dumps(yaml_data, ensure_ascii=False)
		print(f'解析替换之前：{yaml_data_str}')
		# _ 在for循环中表示展位符，没有实际含义，后续代码也不会用到这个变量
		for _ in range(yaml_data_str.count('${')):
			if '${' in yaml_data_str and '}' in yaml_data_str:
				# 获取要切片的开始和结束索引
				start_index = yaml_data_str.index('$')
				end_index = yaml_data_str.index('}', start_index)
				# 开始进行切片操作
				variable_data = yaml_data_str[start_index:end_index + 1]
				print(f'切片获取的引用函数变量：{variable_data}')

				# 使用正则表达式提取 variable_data 变量中，函数的名称 和 对应的参数
				match = re.match(r'\$\{(\w+)\((.*?)\)\}', variable_data)
				print(f'---正则匹配返回---：{match.groups()}')
				if match:
					# 字符串形式的：函数名 + 函数的参数
					func_name, func_params = match.groups()
					# 将获取到的函数参数进行分割操作
					if func_params:
						func_params = func_params.split(',')
					# print(f'func_params:{func_params}')
					else:
						func_params = []
					# 利用获取的到函数名称和参数列表，使用面向对象的 反射来调用函数，获取到函数的执行结果
					extract_data = getattr(DebugTalk(), func_name)(*func_params)
					print(f'提取到结果：{extract_data}')
					# 将原始字符串 yaml_data_str 中的 函数变量引用部分 替换为  反射---函数的执行结果
					# re.escape()函数:用于将一个字符串中的特殊字符转义成正则表达式中的普通字符
					yaml_data_str = re.sub(re.escape(variable_data), str(extract_data), yaml_data_str)
		# 还原数据，将其转换为字典类型：str====>dict
		print(f'解析替换之后：{yaml_data_str}')
		try:
			data = json.loads(yaml_data_str)
		except json.JSONDecodeError:
			data = yaml_data_str

		return data


if __name__ == '__main__':
	s1 = YamlReader(r'../data/adduser.yml')
	datas = s1.read_yaml()[0]
	r1 = RequestsBase()
	r1.parse_and_replace_variables(datas)
