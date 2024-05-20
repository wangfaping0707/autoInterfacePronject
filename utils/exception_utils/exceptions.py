# 自定义异常类
class AssertTypeError(Exception):
	def __init__(self, message='不支持这种断言模式'):
		"""

		:param message: 异常显示的提示信息
		"""
		self.message = message
		# 重构异常
		super().__init__(self.message)
