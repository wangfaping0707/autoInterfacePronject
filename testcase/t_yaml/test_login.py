import pytest

from config import CONF
from utils.YamlUtil import YamlReader

# 获取文件testlogin.yml文件的路径
test_login_file = CONF.get_testlogin_file()
print(test_login_file)
# 使用工具类读取文件内容
test_login_info_list = YamlReader(test_login_file).read_yaml()
print(test_login_info_list)

# 参数化读取配置文件内容
@pytest.mark.parametrize('login_info', test_login_info_list)
def test_get_testlogin_info(login_info):
	print(login_info)


if __name__ == '__main__':
    pytest.main()