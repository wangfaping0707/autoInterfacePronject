import pytest

"""
不带参数运行，打印默认值
pytest testcase/t_args/test_auth_demo.py

带参数运行，打印输入的参数值
pytest --auth username=iTesting  testcase/t_args/test_auth_demo.py
"""


class TestDemo:
	def test_sercet_auth(self, auth):
		print(f'你的鉴权信息为：{auth}')
		assert 1
