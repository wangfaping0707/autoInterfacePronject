import os
import time

import pytest


# 定义测试类
class TestParams:
	# 定义测试数据
	data_list = ['王小明', '陈婫亮', '韩梅明', '李志杰']

	# 定义测试方法,单个参数
	@pytest.mark.parametrize('name', data_list)
	def test_params_one(self, name):
		print('-----test_params_one方法在运行-----')
		print(name)
		assert 1

	# 列表嵌套字典
	datatest07 = [{"user": "zhangsan", "password": "111111111"}, {"user": "lisi", "password": "222222"}]

	@pytest.mark.parametrize("data", datatest07)
	def test_07(self, data):
		print(data)
		print(data["user"], data["password"])
