"""
xunit-style的特点：就是setup和teardown等函数
1、fixture的名字是固定的；
2、前置准备代码 和 后置准备代码 是分开的两个函数；
3、每一个级别的fixture都有对应的函数；
4、自动调用；

fixture：
1、没有固定的名字-----自定义
     @pytest.fixture 来装饰函数
2、前置代码 和 后置代码-----放在一个函数中
     使用yield关键字
3、每个级别都没有固定的 fixture
定义的时候，设置级别
scope：function(测试用例及测试方法)  class(测试类) module(测试模块)  package(测试包)  session(测试会话)
默认 scope=functioon
4、需要做设置才会自动调用

调用方式：
1、在测试用例/测试类上面：
	@pytest.mark.usefixtures('fixture的函数名称')
2、不同作用域的夹具，用在不同的位置
	比如class级别的，就不要用在测试用例上面，而是要用在测试类上面
3、测试用例接收fixture的返回值：
	fixture的函数名称，作为测试用例的参数
	在这种情况下，函数名称对应的变量就接收了fixture的返回值
	同时，
	如果执行测试用例的时候，fixture并未调用，会先调用fixture得到返回值，如果已经执行了fixture函数，直接获取返回值，不会重复调用
"""
import pytest
from t_fixture.test_01_login import Login
import random


@pytest.fixture(scope='class')
def my_fixture():
	print('我是前置函数*********')
	# 前置数据返回，如果返回多个指，用逗号隔开
	value = random.randint(1, 100)
	yield value
	print('我是后置函数................')

@pytest.fixture()
def fix_func():
	print('==========》测试函数级别的------前置《=============')
	yield
	print('==========》测试函数级别的------后置《=============')


all_datas = [
	{"user": "jianshen", "passwd": "12345678", "check": "恭喜,登录成功！"},
	{"user": None, "passwd": False, "check": "用户名或密码类型不正确"},
	{"user": "jia", "passwd": "12345678", "check": "用户名长度小于4"},
	{"user": "jianshen", "passwd": "12345", "check": "密码长度小于6"}
]

@pytest.mark.usefixtures('my_fixture')
class TestLogin:

	@pytest.mark.usefixtures('fix_func')
	@pytest.mark.parametrize('case', all_datas)
	def testLogin(self, case, my_fixture):       # my_fixture接收 my_fixture夹具的返回值
		print(f'接收到my_fixture夹具的返回值为：{my_fixture}')
		res = Login(case.get("user"), case.get("passwd"))
		assert res == case.get("check")

	def test_01_demo(self):
		print('函数正在运行中。。。。。。。。。。。。')
