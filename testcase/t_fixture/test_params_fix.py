import pytest
from t_fixture.test_01_login import Login
import random

all_datas = [
	{"user": "jianshen", "passwd": "12345678", "check": "恭喜,登录成功！"},
	{"user": None, "passwd": False, "check": "用户名或密码类型不正确"},
	{"user": "jia", "passwd": "12345678", "check": "用户名长度小于4"},
	{"user": "jianshen", "passwd": "12345", "check": "密码长度小于6"}
]


@pytest.mark.usefixtures('class_fix')
class TestLogin:

	@pytest.mark.parametrize('case', all_datas)
	def testLogin(self, case, class_fix):  # my_fixture接收 my_fixture夹具的返回值

		res = Login(case.get("user"), case.get("passwd"))
		assert res == case.get("check")

	def test_01_demo(self):
		print('函数正在运行中。。。。。。。。。。。。')


def test_1001_demo():
	print('测试类之外的函数。。。。。')

