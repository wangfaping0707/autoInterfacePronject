from utils.YamlUtil import YamlReader
import re
import random
import time


class DebugTalk:

	def get_extract_data(self, node_name, out_format=None):
		"""
		读取 extract.yml文件 的数据，然后判断 sub_node_name 是否为数字，如果为数字，说明data返回类型为列表，需要走索引取数方法，
		如果不是数字，说明data返回类型为字典，就直接获取下一个节点的value。
		:param node_name: extract.yml文件中的 key
		:param out_format: str类型， 0 随机取列表中的数据 -1 读取列表全部数据，返回值为字符串，-2 读取全部，返回值为列表
		            非 0 -1 -2 则按照顺序读取
		:return:
		"""
		# 调用yaml工具类中，专门读取extract.yml文件的方法，且先读取第一个节点数据
		data = YamlReader(r'./extract.yml').get_extract_yaml(node_name)
		# 正则表达式判断是否为一个数字
		if out_format is not None and bool(re.search(r'^[+-]?\d+$', str(out_format))):
			out_format = int(out_format)
			if out_format == 0:
				return random.choice(data)
			elif out_format == -1:
				return ",".join(data)
			elif out_format == -2:
				return data
			else:
				return self.seq_read(data, out_format)
		# 如果第二个参数不为空且不为数字，则需要在取值
		elif out_format is not None:
			data = data[out_format]
		return data

	# 按照顺序读取列表中的顺序
	def seq_read(self, data, randoms):
		"""获取extract.yml文件中， 第二个参数不为0， -1， -2的情况下"""
		if randoms not in [0, -1, -2]:
			return data[randoms - 1]
		else:
			return None

	# 返回当前系统时间戳
	def get_current_timestamp(self):
		return time.time()

	# 获取请求头
	def get_headers(self, params_type):
		"""
		获取请求头类型
		:param       params_type: 请求参数类型，如 json 或 data
		:return:
		"""
		headers_dict = {
			'data': {'Content-Type': 'application/x-www-formurlencoded;charset=UTF-8'},
			'json': {'Content-Type': 'application/json;charset=UTF-8'}
		}
		header = headers_dict.get(params_type)
		if header is None:
			raise ValueError('不支持其它类型的请求头设置')
		return header


if __name__ == '__main__':
	db = DebugTalk()
	# print(db.get_current_timestamp())
	res = db.get_extract_data('goodids', '2')
	print(res)
