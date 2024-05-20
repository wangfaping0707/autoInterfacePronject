"""
生成器：用来生成id，可以控制测试用例的执行顺序
"""


def generate_module_id():
	# 生成模块id
	for i in range(1, 50000):
		module_id = 'M' + str(i).zfill(4) + '-'
		yield module_id


def generate_case_id():
	# 生成测试用例id
	for i in range(1, 50000):
		case_id = 'C' + str(i).zfill(4) + '-'
		yield case_id


m_id = generate_module_id()
c_id = generate_case_id()









