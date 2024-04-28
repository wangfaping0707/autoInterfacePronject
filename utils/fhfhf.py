import re


def add():
	name = 'baidu'
	print(name)
	if 55:
		name = 'nihao'
	return name
did = {'s': 12, 'f': 454}


if __name__ == '__main__':
	print(add())
	print('Hello World'[::-1])
	print(did.get('ee', '没找到'))
	print(int('-2'))
	print('-----------------------')
	test_pattern = r"\d{2}年"
	# 待匹配的字符串
	test = "18年2019年2020年"
	print(re.match(test_pattern, test))
	# print(re.match(test_pattern, test).group())
	print(re.search(test_pattern, test))
	print(re.search(test_pattern, test).group())
	loo = [1,2,3,4,5]
	print(*loo)
	print(re.escape(r'${get_current_timestamp()}')
)
