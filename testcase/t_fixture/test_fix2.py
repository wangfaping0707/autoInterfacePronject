import pytest


@pytest.fixture(autouse=True)
def fix1():
	print('我是fix1函数。。。。。。。。。。。。')


@pytest.fixture()
def fix2():
	print('我是fix2函数-------------------------')


@pytest.fixture()
def fix3():
	print('我是fix3函数**************************')
	yield
	print('正在关闭中')


def test_fix_01(fix3, fix2):
	pass
