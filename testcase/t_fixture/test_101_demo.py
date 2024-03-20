"""
原文链接：https://blog.csdn.net/seanyang_/article/details/128957344

fixture 与 parametrize 结合实现参数化
如果测试数据需要在 fixture 方法中使用，同时也需要在用例中使用，可以让 parametrize 的 indirect 参数为 True

def parametrize(self, argnames, argvalues, indirect=False, ids=None, scop=None):
indirect = True，pytest 会把 argnames 当做函数执行，将 argvalues 作为参数传入到 argnames
"""
import pytest

# 方法名作为参数
test_user_data = ['Tom', 'Jerry']


@pytest.fixture(scope='module')
def login_r(request):
	# 通过 request.param 获取参数
	user = request.param
	print(f"/n 登录用户： {user}")
	return user


@pytest.mark.parametrize("login_r", test_user_data, indirect=True)
def test_login(login_r):
	a = login_r
	print(f"用例中 login 的返回值； {a}")
	assert a != ""

# 综上，当 indirect = True 时，会将 login_r 作为函数，test_user_data 作为参数传入 login_r 中，
# 生成多条测试数据。通过 return 将结果返回。当调用 login_r 可以获取到 login_r 这个方法的返回数据。












