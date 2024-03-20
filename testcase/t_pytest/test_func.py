import pytest
import allure


class TestFunc:
	def setup_class(self):
		print('---------setup_class方法正在执行中-----------')

	def teardown_class(self):
		print('---------teardown_class方法正在执行中-----------')

	def setup(self):
		print('---------setup方法正在执行中-----------')

	def teardown(self):
		print('---------teardown方法正在执行中-----------')

	@allure.title('a方法的测试用例')
	def test_a(self):
		print('test_a方法正在执行')

	@allure.title('b方法的测试用例')
	def test_b(self):
		print('test_b方法正在执行')


if __name__ == '__main__':
	pytest.main(['-vs', 'test_func.py'])
