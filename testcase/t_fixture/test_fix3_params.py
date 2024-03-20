import pytest


@pytest.fixture(params=['你好', '我好', '大家好'])
def init_data(request):
	print(f'fixture函数正在初始化数据: {request.param}')
	return request.param


def test_init_data(init_data):
	print('功能函数正在执行中。。。。。。。。。')
	print(f'init_data:{init_data}')
	assert init_data in ['你好', '我好', '大家好']
