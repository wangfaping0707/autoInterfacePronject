"""
多个参数的参数化应用：被参数化的是字符串

"""
import pytest

list_user = ['王晓兰', '陈灵玉', '汤贤达', '司马空']
list_pwd = ['test123', 'test456', 'test789', 'test000']


@pytest.mark.parametrize('password', list_pwd)
@pytest.mark.parametrize('user', list_user)
def test_get_info(user, password):
	print(f'账户信息：姓名{user}  密码{password} ')







