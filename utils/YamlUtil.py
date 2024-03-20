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

	def read_yaml(self):
		if not self.data:
			with open(self.yaml_file, mode='rt', encoding='utf-8') as f:
				self.data = list(yaml.safe_load_all(f))
		return self.data
