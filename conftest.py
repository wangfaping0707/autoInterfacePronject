import pytest


@pytest.fixture(scope='session', autouse=True)
def session_fixture():
	print("==========全局级======准备工作========")
	yield
	print("==========全局级======结束工作========")


@pytest.fixture(scope='class', params=['edge', 'firefox', 'google'])
def class_fix(request):
	print(f'在{request.param}浏览器当中去运行测试用例。。。。。')
	print(f'测试用例来源于那个类，{request.cls}')
	print(f'使用在调用，{request.scope}')

# # 开始执行测试方法之前，先清除中间文件中的数据，即是清空数据方法
# @pytest.fixture(scope='session', autouse=True)
# def clear_yaml(file):
# 	with open(file=file, mode='w', encoding='utf-8') as f:
# 		print('我正在执行数据清理工作。。。。。。。。。。。。。。。。。')
# 		f.truncate()
