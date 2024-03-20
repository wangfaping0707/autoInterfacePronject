import pytest
import allure


@allure.epic("项目名称：源计划——自动化测试")
@allure.feature("模块名称：订单模块")
class TestAllureDemo:
	@allure.severity(allure.severity_level.BLOCKER)
	@allure.story("用例名称：商品购买")
	@allure.title("用例标题：购买")
	def test_01(self):
		print('test_01函数正在运行中。。。。。。。')
		assert 1 == 1

	@allure.severity(allure.severity_level.CRITICAL)
	@allure.story("用例名称：订单支付")
	@allure.title("用例标题：支付")
	def test_02(self):
		print('test_02函数正在运行中。。。。。。。')
		assert 2 == 2

	@allure.severity(allure.severity_level.MINOR)
	@allure.story("用例名称：订单发货")
	@allure.title("用例标题：物流")
	def test_03(self):
		print('test_03函数正在运行中。。。。。。。')
		assert 3 == 3

	@allure.story("用例名称：用例标题动态变化")
	@allure.description("验证动态变化参数")
	@pytest.mark.parametrize('name', ['王晓涵', '康利智', '陈诗雨'])
	def test_get_info(self, name):
		with allure.step("测试步骤一"):
			print(name)
		with allure.step("测试步骤二"):
			print("allure学习中。。。。。")
		allure.attach()
		allure.dynamic.title(name)