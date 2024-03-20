import pytest
"""
考虑场景：
我们的自动化用例需要支持在不同测试环境运行，有时候在dev环境运行，有时候在test环境运行；
有时候需要根据某个参数不同的参数值，执行不同的业务逻辑；

上面的场景我们都可以通过“在命令行中输入参数，然后用例中接收这个参数，通过判断这个参数的值来做不同的逻辑”来实现。
那么我们的需求就变为pytest中如何自定义一个命令行参数呢？这时候我们就需要用到pytest的钩子函数：pytest_addoption

通过conftest.py配置
新建一个conftest.py文件，然后在conftest.py文件中通过pytest_addoption方法来添加命令行参数，通过定义的fixture来获得参数的值。

https://blog.csdn.net/python_tian/article/details/120313952

"""

# 自定义运行命令行参数，并将其添加到配置对象中
def pytest_addoption(parser):
	parser.addoption(
		"--auth", action="store", default="你好我是默认值，佛门中人嘻嘻哈哈", help="请输入你的鉴权"
	)

	# 注册自定义参数cmdopt到配置对象
	parser.addoption(
		"--cmopt", action="store", default="默认值1", help="my option: type1 or type2"
	)

	# 注册自定义参数env到配置对象
	parser.addoption(
		"--env", action="store", default="dev", help="env：表示测试环境，默认dev环境"
	)



# 从配置对象中获取自定义的命令行参数,第一种方式
@pytest.fixture(scope='session')
def auth(request):
	return request.config.getoption('--auth')

"""
下面conftest.py文件中新增了两个命令行参数：–cmdopt和–env；
然后定义了两个fixture，在测试用例中想要获得参数–cmdopt的值，
就可以调用cmdopt函数；调用env函数可以获取参数–env的值。
"""


# 第二种方式：获取自定义的命令行参数
@pytest.fixture(scope='session')
def cmopt(pytestconfig):
	# 从配置对象获取cmdopt的值
	return pytestconfig.getoption("cmopt")

@pytest.fixture(scope='session')
def env(request):
	# 从配置对象获取env的值
	return request.config.getoption("--env")















