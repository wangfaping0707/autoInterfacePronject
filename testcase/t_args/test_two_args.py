import pytest
"""
不带参数运行：
命令行中输入指令：pytest test_option.py 

因为我们在conftest.py文件中定义的参数env的默认值为dev，所以当运行时命令行不传env参数，则使用默认值dev。

带参数运行：
命令行中输入指令：pytest test_option.py -s --env=test
从结果中可以看到，命令行中输入参数env=test，在测试用例中获取到通过fixture获取到env的值为test
"""

class TestAgrs():
	def test_env_demo(self, env):
		if env == 'dev':
			print("当前测试环境为：{}，域名切换为开发环境".format(env))
		elif env == 'test':
			print(f"你当前所在的测试环境为：{env}")
		elif env == 'uat':
			print(f"hello，霓虹，你所在测试环境为：{env}")
		else:
			print("环境错误，当前环境{}不存在".format(env))
		# assert 1

