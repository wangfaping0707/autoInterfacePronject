import os
import time

import pytest

if __name__ == '__main__':
	# pytest.main(['testcase/t_pytest/test_params_one.py'])
	# pytest.main(['testcase/t_fixture/test_fix3_params.py'])
	# pytest.main(['testcase/t_allure/test_allure_demo.py'])
	pytest.main(['testcase/t_allure/test_allure1.py'])
	time.sleep(3)
	os.system("allure generate outputs/allure_results_files -o outputs/html/reports.html --clean")
	time.sleep(5)
	# 自动打开测试报告
	os.system("allure open ./outputs/html/reports.html")

