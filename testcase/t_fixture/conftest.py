"""
想要与其它测试模块共享的fixture，统一放到这个模块

1、测试模块当中，不需要导入 conftest.py ，直接调用里面的fixture

2、会自动的去 conftest.py 当中去找fixture

3、可以创建多个不同层级的 conftest.py文件


怎么一个找法？顺序是什么样的？
conftest.py-----生效范围是多少？

conftest.py在哪个python包下面，这个python包下面的所有测试用例全部可以自动调用它里面的fixture函数

测试模块当中，再去查找fixture的过程中，是一个什么顺序？
1、先看自己的模块有没有，如果有，直接使用
2、如果没有呢，就在当前所在的python包当中找conftest.py，在它里面找有木有fixture，如果找到了，就直接使用
3、如果2中没有，继续上一层，重复2的方式。。。。。
直到rootdir为止


"""
import pytest
import random


@pytest.fixture(scope='module')
def test_fixture_conftest():
	print('这是在conftest模块中的前置函数。。。。。。。。。。。。。')
	val = random.randrange(20, 50)
	yield val
	print('我在这里啊。。。。。conftest模块中的后置函数。。。。。。。。。。。。。')


@pytest.fixture(scope='function')
def func_fix():
	print('2023/12/07 我在学习fixture函数中。。。。')
	value = random.uniform(1, 9)
	yield value
	print('只为最后的胜利。。。。。。。。。。。。。')





















