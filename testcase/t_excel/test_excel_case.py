from config.CONF import get_excel_data1, ConfigYaml
from common.ExcelData import ReaderExcelData
from utils.LogUtil import my_log
from common.ExcelConfig import DataConfig
import re

# 初始化excel文件相关信息
# 1、找到要读取的excel文件路径
case_excel_path_file = get_excel_data1()
print(case_excel_path_file)
# 2、找到excel中，要读取sheet表中的数据
sheet_name = ConfigYaml().get_excel_sheet()
print(sheet_name)
# 3、运行读取excel表格中数据
read_excel_obj = ReaderExcelData(case_excel_path_file, sheet_name)
data_info = read_excel_obj.get_run_data()
print(data_info)
# 4、记录运行日志
log = my_log()

# 默认正则表达式样式
p_mode = '\${(.*)}\$'


# 匹配字符串格式方法
def res_find(data, pattern=p_mode):
	"""
	匹配特定格式的字符串
	:param data: 被匹配的字符串
	:param pattern: 匹配的规则，即是正则表达式
	:return:
	"""
	pattern = re.compile(pattern)
	re_res = pattern.findall(data)
	return re_res


# 匹配特定字符串-然后对匹配出来的字符串-进行子字符串替换
def res_sub(data, replace, pattern=p_mode):
	"""
	替换
	:param data:要被匹配的原始字符串
	:param replace: 替换的子字符串
	:param pattern:  匹配模式，即正则表达式
	:return:
	"""
	pattern = re.compile(pattern)
	re_res = pattern.findall(data)
	if re_res:
		return re.sub(pattern, replace, data)
	return re_res


# 5、测试用例方法，参数化运行
# 一个用例的执行
class TestExcel:
	# 读取信息
	def test_run(self):
		data_key = DataConfig
		# 获取第一个参数
		p_name = data_info[1][DataConfig.name]
		print(p_name)


if __name__ == '__main__':
	print(res_find('{"Authorizations":"JWT ${token}$"}'))
	print(res_sub('{"Authorizations":"JWT ${token}$"}','2023-11-29 18:57'))
