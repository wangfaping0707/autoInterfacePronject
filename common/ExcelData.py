from utils.ExcelUtil import ExcelReader
from common.ExcelConfig import DataConfig
from config.CONF import ConfigYaml, get_excel_data1


class ReaderExcelData:
	def __init__(self, excel, sheet_name):
		# 新建一个读取excel数据的对象
		# self.reader = ExcelReader('../data/data1.xlsx', '个人信息表')
		self.reader = ExcelReader(excel, sheet_name)

	# print(reader.read_excel())

	def get_run_data(self):
		"""
		筛选出已经结婚的信息
		:return:
		"""
		marry_list = []
		for d in self.reader.read_excel():
			if d[DataConfig().is_marry] == '已':
				marry_list.append(d)
		return marry_list


if __name__ == '__main__':
	read = ReaderExcelData(get_excel_data1(), ConfigYaml().get_excel_sheet())
	print(read.get_run_data())
