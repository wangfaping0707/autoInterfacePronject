import os

import xlrd


# 目的：参数化，pytest=》@pytest.mark.parametrize只能读取类型为列表的数据

# 1、验证要读取的文件是否存在
class ExcelReader:
	def __init__(self, excel_file, sheet_by):
		"""
		:param excel_file: 要读取工作薄
		:param sheet_by: 根据索引还是sheet名称来选择要读取的表
		"""
		if os.path.exists(excel_file):
			self.excel_file = excel_file
			self.sheet_by = sheet_by
			self.list_data = list()
		else:
			raise FileNotFoundError('读取的文件不存在')

	# 读取excel表格中数据的方法:读取sheet的方式，是sheet名称还是索引
	def read_excel(self):
		# 先判断文件中的数据是否已读取，如已读取，则不再读取
		if not self.list_data:
			# 打开工作薄对象
			work_book = xlrd.open_workbook(self.excel_file)
			# 判断是通过sheet名称读取还是sheet索引读取对应的sheet表
			if type(self.sheet_by) not in [str, int]:
				raise TypeError('请输入int类型或str类型')
			elif type(self.sheet_by) == int:
				sheet = work_book.sheet_by_index(self.sheet_by)
			elif type(self.sheet_by) == str:
				sheet = work_book.sheet_by_name(self.sheet_by)
			# 开读取sheet表中的数据
			# 取出excel表格中表头，即固定字段列
			excel_title = sheet.row_values(rowx=0, start_colx=0, end_colx=None)
			# 遍历除首行以外其他行数据，然后与首行组成字典
			for r in range(1, sheet.nrows):
				excel_value = sheet.row_values(r)
				# 表格首行和数值行组成字典,然后放到列表中：@pytest.mark.parametrize只能读取类型为列表的数据，所以要放到列表
				dict_data = dict(zip(excel_title, excel_value))
				self.list_data.append(dict_data)
		return self.list_data


if __name__ == '__main__':
	reader = ExcelReader('../data/data1.xlsx', "个人信息表")
	print(reader.read_excel())
