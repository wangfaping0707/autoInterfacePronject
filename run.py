import os
import time
import shutil
import pytest

if __name__ == '__main__':
	# pytest.main(['testcase/t_pytest/test_params_one.py'])
	# pytest.main(['testcase/t_fixture/test_fix3_params.py'])
	# pytest.main(['testcase/t_allure/test_allure_d2.py'])
	# 执行allure文件代码
	# pytest.main(['-vs','testcase/t_allure'])
	# pytest.main(['-vs', 'testcase/cases/test_login.py'])
	# pytest.main(['-vs', 'testcase/cases'])
	pytest.main(['-vs', 'testcase/t_allure'])
	shutil.copy('./environment.xml','./outputs/allure_results_files')
	# os.system("allure generate ./outputs/allure_results_files -o outputs/html/reports.html --clean")
	# time.sleep(5)
	# 自动打开测试报告
	# os.system("allure open ./outputs/html/reports.html")
	# os.system("allure serve ./outputs/allure_results_files")

