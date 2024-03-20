"""
pytest_collection_modifyitems 是在用例收集完毕之后被调用，可以用来调整测试用例执行顺序；
它有三个参数，分别是：

session：会话对象；
config：配置对象；
items：用例对象列表；改变items里面用例的顺序就可以改变用例的执行顺序了

这三个参数分别有不同的作用，都可以拿来单独使用，修改用例执行顺序主要是使用 items 参数【用例执行之前，收集到的测试用例会以元素对象的方式存放在用例对象列表items中】
"""

# 在收集完测试用例后才会执行
import pytest
import time


def pytest_collection_modifyitems(items):
	print('pytest 收集到的所有测试用例：\n', items)
	start_time = time.time()
	print(f'开始执行时间{time.time()}')
	for item in items:
		print('---' * 10)
		print('用例名：', item.name)
		print('用例节点：', item.nodeid)
	end_time = time.time()
	print(f'结束执行时间{end_time}')
	print(f'花费时间{end_time - start_time}')


if __name__ == '__main__':
	pytest.main(['-s'])
