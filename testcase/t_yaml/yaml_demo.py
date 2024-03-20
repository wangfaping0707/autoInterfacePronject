"""
1、创建yaml格式文件
2、读取这个文件
	2.1、导入yaml包
	2.2、打开文件
	2.3、使用yaml读取文件
3、输出这个文件
"""
import yaml

# 读取单个文件
with open('./data.yml', mode='r', encoding='utf-8') as f:
	res1 = yaml.safe_load(f)
	print(type(res1))
	# res2 = yaml.load(stream=f, Loader=yaml.FullLoader)
	print(f'res1:{res1}')
# print(f'res2:{res2}')

print('----------------分割线---------')
# 读取多个文件
with open('./data1.yml', mode='r', encoding='utf-8') as f:
	res3 = yaml.safe_load_all(f)
	print(type(res3))
	print(list(res3))
	# 	res3 是迭代器，所以需要循环取值
	for i in res3:
		print(i)

# 写入yaml数据到文件
yml_data = ["蓝色", 1234, "green", {"name": "肖雨涵", "age": 18, "sex": "female"}, ['a', 'b', 'c'], "game_over"]


# --------写入数据的方法
def write_yaml(data, file):
	with open(file, mode='wt', encoding='utf_8') as f:
		# yaml.dump(data=data, stream=f, allow_unicode=True)
		print('我正在执行写入操作。。。。。。。。。。。')
		yaml.safe_dump(data=data, stream=f, allow_unicode=True)


# 清空数据方法
def clear_yaml(file):
	with open(file=file, mode='w', encoding='utf-8') as f:
		print('我正在执行数据清理工作。。。。。。。。。。。。。。。。。')
		f.truncate()


if __name__ == '__main__':
	write_yaml(yml_data, 'data3.yml')
	# clear_yaml('./data3.yml')
