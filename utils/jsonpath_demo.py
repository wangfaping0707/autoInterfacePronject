"""
一 什么是jsonpath
   jsonpath是python的一个第三方工具库，专门用来解析json数据的，可以根据表达式来抽取json数据中指定的数据值。它的作用就相当于XPath对于XML。
   jsonpath属于第三方库，需要进行安装方可使用，如下: pip install jsonpath

二 jsonpath的使用
1. jsonpath 函数参数
我们在使用jsonpathd的时候一般是使用它里面的jsonpath函数，即jsonpath.jsonpath()。

jsonpath()接受5个参数，如下 : jsonpath(obj, expr, result_type='VALUE', debug=0, use_eval=True)

obj：要搜索的 JSON 对象。
expr：JSONPath 表达式，用于指定要提取的值的路径。
result_type：可选参数，用于指定返回结果的类型。默认为 ‘VALUE’，表示返回匹配到的值；
            还可以选择 ‘PATH’，表示返回匹配到的路径；或者选择 ‘BOTH’，表示同时返回匹配到的值和路径。
debug：可选参数，用于控制调试模式。默认为 0，表示关闭调试模式；设置为 1，则会在控制台输出调试信息。
use_eval：可选参数，用于指定是否使用 eval() 函数来计算表达式。默认为 True，表示使用 eval()；设置为 False，则会使用更安全的方式来计算表达式。
其中obj 和 expr 是必须参数，即要处理的json数据对象和提取表达式，常用的就是这两个参数，其他参数可以根据个人需要赋值

文章：https://blog.csdn.net/qq_44690947/article/details/131876399
"""
import jsonpath
data = {
	"store": {
		"book": [
			{"category": "reference",
			 "author": "Nigel Rees",
			 "title": "Sayings of the Century",
			 "price": 8.95
			 },
			{"category": "fiction",
			 "author": "Evelyn Waugh",
			 "title": "Sword of Honour",
			 "price": 12.99
			 },
			{"category": "fiction",
			 "author": "Herman Melville",
			 "title": "Moby Dick",
			 "isbn": "0-553-21311-3",
			 "price": 8.99
			 },
			{"category": "fiction",
			 "author": "J. R. R. Tolkien",
			 "title": "The Lord of the Rings",
			 "isbn": "0-395-19395-8",
			 "price": 22.99
			 }
		],
		"bicycle": {
			"color": "red",
			"price": 19.95
		}
	}
}

# 提取bicycle节点
# [{'color': 'red', 'price': 19.95}]
bcy = jsonpath.jsonpath(data, '$..bicycle')
print(f'bcy:{bcy}')

# 提取book中含有isbn的节点数据   ?() ： 支持过滤操作     （）：支持表达式
# [{'category': 'fiction', 'author': 'Herman Melville', 'title': 'Moby Dick', 'isbn': '0-553-21311-3',
# 'price': 8.99}, {'category': 'fiction', 'author': 'J. R. R. Tolkien',
# 'title': 'The Lord of the Rings', 'isbn': '0-395-19395-8', 'price': 22.99}]

isbn = jsonpath.jsonpath(data, '$..book[?(@.isbn)]')
print(isbn)

# 提取单个字段值author
# ['Nigel Rees', 'Evelyn Waugh', 'Herman Melville', 'J. R. R. Tolkien']
author = jsonpath.jsonpath(data, '$..author')
print(author)

# 提取bicycle中color,price
color = jsonpath.jsonpath(data, '$..bicycle.color')
# ['red']
price = jsonpath.jsonpath(data, '$..bicycle[price]')
# price = jsonpath.jsonpath(data, '$..bicycle.price')
print(f'price:{price}')
# [19.95]


# 提取book中第2个子节点数据
book1 = jsonpath.jsonpath(data, '$..book[1]')
# [{'category': 'fiction', 'author': 'Evelyn Waugh', 'title': 'Sword of Honour', 'price': 12.99}]

# 提取book中前2个子节点数据
book2 = jsonpath.jsonpath(data, '$..book[:2]')
# [{'category': 'reference', 'author': 'Nigel Rees', 'title': 'Sayings of the Century', 'price': 8.95}, {'category': 'fiction', 'author': 'Evelyn Waugh', 'title': 'Sword of Honour', 'price': 12.99}]

# 提取book中price小于15的节点数据
price = jsonpath.jsonpath(data, '$..book[?(@.price<15)]')
# [{'category': 'reference', 'author': 'Nigel Rees', 'title': 'Sayings of the Century', 'price': 8.95}, {'category': 'fiction', 'author': 'Evelyn Waugh', 'title': 'Sword of Honour', 'price': 12.99}, {'category': 'fiction', 'author': 'Herman Melville', 'title': 'Moby Dick', 'isbn': '0-553-21311-3', 'price': 8.99}]

# 表达式参数化
#节点数据参数化
arg = 'book'
#提取book前三个子节点的price值
price = jsonpath.jsonpath(data, f'$..{arg}[:3].price')
#[8.95, 12.99, 8.99]

"""
三 jsonpath使用注意事项
jsonpath操作的对象是一个json对象或者python中的字典dict。
jsonpath返回数据是一个列表list。如果一个key有多个value, 按匹配顺序依次存到list中返回。
jsonpath 的表达式参数可以参数化。
"""
