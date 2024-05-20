# 定义一个读yaml数据的工具类
import os
import yaml


class YamlReader:
	def __init__(self, yaml_file):
		if os.path.exists(yaml_file):
			self.yaml_file = yaml_file
		else:
			raise FileNotFoundError("文件不存在")
		self.data = None

	# 读取单个文件
	def read_yaml(self):
		testcase_list = []
		if not self.data:
			with open(self.yaml_file, mode='rt', encoding='utf-8') as f:
				self.data = yaml.safe_load(f)
				# 处理一个yaml文件多条测试用例的场景
				if len(self.data) <= 1:
					baseinfo = self.data[0].get('baseinfo')
					print(baseinfo)
					# 循环迭代取出case 分别与 baseinfo进行组合
					for tc in self.data[0].get('testCase'):
						params = [baseinfo, tc]
						testcase_list.append(params)
					print(testcase_list)
					return testcase_list
				else:
					# print(self.data)
					return self.data

	# 读取多个文件
	def read_yamls(self):
		if not self.data:
			with open(self.yaml_file, mode='rt', encoding='utf-8') as f:
				self.data = list(yaml.safe_load_all(f))
		return self.data

	# 读取全局文件extract.yml
	def get_extract_yaml(self, node_name, sub_node_name=None):
		"""
		用于获取 extract.yml 文件的数据
		:param node_name: 第一级的key
		:param sub_node_name:  下一级的key
		:return:
		"""
		# file_path = '../extract.yml'
		try:
			with open(self.yaml_file, mode='r', encoding='utf-8') as f:
				extract_data = yaml.safe_load(f)
				# print(f'extract_data:{extract_data}')
				if sub_node_name is None:
					return extract_data.get(node_name, f'extract.yml文件中没有这个字段信息{node_name}!!!!!')
				else:
					return extract_data.get(node_name, '没有这个键，请核对').get(sub_node_name, '没有这个字键，请核对')
		except yaml.YAMLError as e:
			print(f'Error:读取yaml文件失败，请检查格式-{self.yaml_file}, {e}')
		except Exception as e:
			# print(f'Error: 未知异常-{e}')
			raise e

	# 数据写入extract.yml文件
	def write_extract_yaml(self, data):
		"""
		数据写入到yaml文件
		:param data: 要被写入的数据
		:return:
		"""
		with open(self.yaml_file, mode='a+', encoding='utf-8') as f:
			yaml.safe_dump(data=data, stream=f, allow_unicode=True)


# 返回当前时间的函数


if __name__ == '__main__':
	# print(os.path.exists('../testcase/t_yaml/data4.yml'))
	# # 读取单个文件
	# s1 = YamlReader(r'../testcase/t_yaml/data4.yml')
	# print(s1.read_yaml())

	# print('-------------------------------------------------')
	# # 读取多个文件
	# s2 = YamlReader(r'../testcase/t_yaml/data1.yml')
	# print(s2.read_yamls())

	# print('-----------------------------------------')
	# # print(os.path.exists(r'../extract.yml'))
	# s3 = YamlReader(r'../extract.yml')
	# print(s3.get_extract_yaml('token'))
	# print(s3.get_extract_yaml('Cookie'))
	# print(s3.get_extract_yaml('goodids'))
	# print(s3.get_extract_yaml('Cookie', 'access_token'))
	# print('-------------------------------------------------------')
	# data = {'sex': 'male'}
	# s3.write_extract_yaml(data)
	# print('*********************************************************')
	s4 = YamlReader(r'./test_adduser.yml')
	s4.read_yaml()
	s5 = YamlReader(r'../data/businessScenario/productBusiness.yml')
	s5.read_yaml()
# print(s4.read_yaml())
