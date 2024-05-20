# 练习使用接口封装的方法
from utils.YamlUtil import YamlReader
from utils.apiutils_single import RequestsBase
import os
import pytest
import allure
from utils.generate_id import m_id, c_id

@allure.feature(next(m_id) + "模块名称：登录模块")
class TestLogin:
	"""登录模块"""
	# test_adduser.yml参数文件所在路径
	path = r'./utils/test_adduser.yml'

	@pytest.mark.parametrize('base_info, testcase', YamlReader(path).read_yaml())
	@allure.story(next(c_id) + '用例名称：新增用户')
	def test_login_module(self, base_info, testcase):
		# 在allure报告中显示不同的测试用例名称
		# print(f"执行打印:{testcase['case']}")
		allure.dynamic.title(testcase['case'])
		RequestsBase().execute_test_cases(base_info, testcase)
