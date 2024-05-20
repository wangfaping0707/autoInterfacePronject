import pytest
import time
import datetime
from utils.dingding_rebot.ding_rebot import send_dd_msg
from config.setting import is_dd_msg


@pytest.fixture(scope='session', autouse=True)
def session_fixture():
	print("==========全局级======准备工作========")
	yield
	print("==========全局级======结束工作========")


@pytest.fixture(scope='class', params=['edge', 'firefox', 'google'])
def class_fix(request):
	print(f'在{request.param}浏览器当中去运行测试用例。。。。。')
	print(f'测试用例来源于那个类，{request.cls}')
	print(f'使用在调用，{request.scope}')


# # 开始执行测试方法之前，先清除中间文件中的数据，即是清空数据方法
# @pytest.fixture(scope='session', autouse=True)
# def clear_yaml(file):
# 	with open(file=file, mode='w', encoding='utf-8') as f:
# 		print('我正在执行数据清理工作。')
# 		f.truncate()

# 开始执行测试方法之前，先清除中间文件 extract.yml文件中的数据，即是清空数据方法
# @pytest.fixture(scope='session', autouse=True)
# def clear_extract_data():
# 	with open(r'./extract.yml', mode='w', encoding='utf-8') as f:
# 		print('extract文件数据清理中')
# 		f.truncate()

def format_duration(seconds):
	"""将秒数转换为 时分秒 返回
	在 Python 中使用 DateTime 模块将秒转换为小时、分钟和秒
	Python 提供了一个 DateTime 模块，其中包含用于操作日期和时间的类和函数。 我们可以使用这些类和函数来处理各种任务的日期、时间和时间间隔。
	DateTime 模块提供 timedelta() 函数将秒转换为小时、分钟和秒。 此函数接受参数秒并以格式（小时、分钟和秒）返回它。
	原文链接：https://blog.csdn.net/fengqianlang/article/details/130497174    (0:00:16.190000)
	"""
	return str(datetime.timedelta(seconds=seconds)).split('.')[0]


# print(format_duration(56000))

def pytest_terminal_summary(terminalreporter, exitstatus, config):
	"""
	这个函数是pytest框架中 预定义的钩子函数，用于在测试结束后 自动收集测试用例执行结果
	:param terminalreporter:
	:param exitstatus:
	:param config:
	:return:
	"""
	# terminalreporter.stats:这个是收集测试用例的执行结果
	print(terminalreporter.stats)
	# 用例的总数量
	testcase_total = terminalreporter._numcollected
	print(f'测试用例总数：{testcase_total}')
	# 收集执行通过的测试用例，没有则返回一个空列表
	passed = terminalreporter.stats.get('passed', [])
	# 通过的测试用例数量
	passed_num = len(passed)

	# 收集执行失败的测试用例，没有则返回一个空列表
	failed = terminalreporter.stats.get('failed', [])
	# 失败的测试用例数量
	failed_num = len(failed)

	# 收集错误的测试用例，没有则返回一个空列表
	error = terminalreporter.stats.get('error', [])
	# 错误的测试用例数量
	error_num = len(error)

	# 收集跳过的测试用例，没有则返回一个空列表
	skipped = terminalreporter.stats.get('skipped', [])
	# 跳过执行的用例数量
	skipped_num = len(skipped)

	# 统计所有案例执行时间,并返回小数点为两位的时间
	duratuon = round(time.time() - terminalreporter._sessionstarttime, 2)
	# 以时分秒显示案例执行的秒数
	formattered_duration = format_duration(duratuon)

	# 统计通过率、失败率、错误率
	pass_rate = f'{(passed_num / testcase_total) * 100:.2f}%' if testcase_total > 0 else 'N/A'
	failed_rate = f'{(failed_num / testcase_total) * 100:.2f}%' if testcase_total > 0 else 'N/A'
	error_rate = f'{(error_num / testcase_total) * 100:.2f}%' if testcase_total > 0 else 'N/A'

	summary = f"""
	自动化测试结果，通知如下，具体执行结果：
	测试用例总数：{testcase_total}  
	测试用例通过数：{passed_num}     通过率：{pass_rate}
	测试用例失败数：{failed_num}     失败率：{failed_rate}
	测试用例错误数：{error_num}      错误率：{error_rate}
	测试用例跳过数：{skipped_num}
	执行总时长：{duratuon}s ({formattered_duration})  
	"""
	print(summary)
	if is_dd_msg:
		send_dd_msg(summary)
