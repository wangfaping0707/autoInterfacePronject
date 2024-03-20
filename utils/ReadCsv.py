import csv
import os

"""
CSV（Comma-Separated Values）是一种常用的数据存储格式，它以逗号为分隔符将数据以文本形式存储在文件中。
Python是一门强大的编程语言，提供了许多库和工具，使得读取和处理CSV文件变得非常简便。在本文中，我们将深入介绍如何使用Python读取CSV文件的详细步骤

步骤1：导入所需的库
在开始之前，需要导入Python中处理CSV文件所需的库。Python标准库中的csv模块是一个处理CSV文件的良好选择。
import csv

步骤2：打开CSV文件
在读取CSV文件之前，需要使用Python的内置open函数打开文件。确保提供正确的文件路径，并指定文件的打开模式为读取（‘r’）
file_path = 'your_file.csv'

with open(file_path, 'r') as csv_file:
    # 后续操作将在此代码块中进行

步骤3：创建CSV读取器
在打开文件后，需要创建一个CSV读取器对象，用于我们逐行读取CSV文件的内容。
with open(file_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    for row in csv_reader:
        # 每次迭代将读取一行数据并存储在'row'变量中

步骤4：处理CSV数据
现在我们可以通过迭代CSV读取器对象来访问每一行数据。每一行数据都被解析为一个由字段组成的列表。
with open(file_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)    
    for row in csv_reader:
        # 您可以通过索引访问每个字段
        # 例如：第一个字段 row[0], 第二个字段 row[1], 依此类推
        
        # 进行您的数据处理操作，例如打印每一行数据
        print(row)

步骤5：使用CSV DictReader

如果CSV文件的第一行包含列标题，
我们还可以使用csv.DictReader来创建一个能够返回每行数据作为字典的读取器。
这样做使得我们可以通过列标题访问数据，使得代码更加清晰易读。

with open(file_path, 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    
    for row in csv_reader:
        # 可以通过列标题访问每个字段
        # 例如：row['Name'], 依此类推
        
        # 进行数据处理操作，例如打印特定字段的值
        print(row['Name'])
"""


class ReaderCsv:
	def __init__(self, file):
		if os.path.exists(file):
			self.file = file
		else:
			raise FileNotFoundError('读取的文件不存在')

	def read_csv1(self):
		with open(self.file, mode='rt', encoding='utf-8') as f:
			contents = csv.reader(f)
			# print(f'contents:{type(contents)}')
			for content in contents:
				yield content
			# print(content)

	def read_csv(self):
		"""
		使读出来的数据为字典
		:return:
		"""
		with open(self.file, mode='rt', encoding='utf-8') as f:
			contents = csv.DictReader(f)
			for content in contents:
				# print(f'content:{content}')
				yield dict(content)


if __name__ == '__main__':
	# for data1 in ReaderCsv(r'csv_data.csv').read_csv1():
	# 	print(data1)
	for data in ReaderCsv(r'csv_data.csv').read_csv():
		print(data)
