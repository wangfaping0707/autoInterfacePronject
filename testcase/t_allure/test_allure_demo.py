import os

import pytest
import allure

@allure.feature("模块名称：这是一个接口测试类")
class TestAllure:
	@allure.title("验证1等于1")
	@allure.description('测试数字大小验证功能函数')
	@allure.story('方法测试：验证数据相等')
	@allure.severity(allure.severity_level.CRITICAL)
	def test_allure_demo1(self):
		assert 1 == 1

	@allure.title("验证函数打印功能")
	@allure.description('test输出函数功能是否正常')
	@allure.story('方法测试：test打印功能')
	@allure.severity(allure.severity_level.BLOCKER)
	def test_allure_demo2(self):
		print('测试allure报告的生成')

	@allure.title("验证1等于3")
	@allure.description('测试数字大小验证功能函数')
	@allure.story('方法测试：验证数据unequal')
	@allure.severity(allure.severity_level.CRITICAL)
	def test_allure_demo3(self):
		assert 1 == 3

	@allure.title("验证1等于6")
	@allure.description('测试数字大小验证功能函数')
	@allure.story('方法测试：验证数据unequal')
	def test_allure_demo4(self):
		assert 1 == 6

	@allure.title("验证6等于6")
	@allure.description('测试数字大小验证功能函数')
	@allure.story('方法测试：验证数据相等')
	def test_allure_demo5(self):
		assert 6 == 6

	@pytest.mark.parametrize('name', ['王晓涵', '康利智', '陈诗雨'])
	def test_get_info(self, name):
		print(name)
		allure.dynamic.title(name)


if __name__ == '__main__':
	pytest.main()
	# pytest.main(['-v','-s','test_allure_demo.py', '--alluredir=/outputs/allure_results_files','--clean-alluredir'])
	# os.system('allure generate /outputs/allure_results_files -o /outputs/allure_results_files/html ')
