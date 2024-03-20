import pytest


# 定义测试类
class TestParamsTwo:
	# 定义测试数据
	data_list = [('王小二', 18), ('李兰兰', 19), ('陈美优', 17), ('成贝贝', 16)]

	# 定义读取个人信息函数,多个参数读取
	@pytest.mark.parametrize(('name', 'age'), data_list)
	def test_get_info(self, name, age):
		print('-----get_info方法-----')
		print(f'个人简要信息,姓名：{name}=====>年龄：{age}')
		assert 1

	@pytest.mark.parametrize("name, age", data_list)
	def test_get_info1(self, name, age):
		print('-----get_info方法-----')
		print(f'个人简要信息,姓名：{name}=====>年龄：{age}')
		assert 1


if __name__ == '__main__':
	pytest.main(['test_params_two.py'])
