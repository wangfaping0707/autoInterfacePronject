# 定义一个普通方法
import pytest


def func(x):
	return x + 3


# 定义pytest的断言方法
def test_a():
	print('正在执行-----test_a的方法-----')
	assert func(1) == 5


def test_b():
	print('正在执行-----test_b的方法-----')
	assert func(2) == 5


if __name__ == '__main__':
	pytest.main(['-s', '-v', 'test_demo.py'])
