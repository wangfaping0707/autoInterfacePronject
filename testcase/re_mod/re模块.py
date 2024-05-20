import re

"""
原文链接：https://blog.csdn.net/tutan123321/article/details/130858487

什么是Python re.search.group?
在Python re.search()函数中，group()方法用于获取匹配的子串。这个方法可以返回与正则表达式匹配的字符串的子串。如果正则表达式中没有分组，则group()函数返回整个匹配字符串。

group()方法可以传入一个参数，这个参数指定要返回的组。如果正则表达式中有多个组，可以使用数字来引用它们。从1开始，每个组都有一个编号。如果没有指定参数，则默认返回整个匹配的字符串。

group()函数非常灵活，可以用于许多不同的应用程序。无论是在文本处理中还是在网页爬虫中，都可以快速应用。

怎样使用Python re.search.group?
使用re.search()函数和group()方法可以快速匹配文本。这些函数可以轻松地搜索一个字符串，并返回与正则表达式匹配的子字符串。以下是一些使用Python re.search.group()的示例：

"""
# 使用group()返回整个匹配字符串
import re

text = "hello world!"
pattern = "hello"

result = re.search(pattern, text)
print(type(result))
print(result)
print(result.group())  # 输出结果为"hello"
print('=========================================')
# 使用group()返回第一个子组
# 在这个示例中，正则表达式“My name is (\w+)”匹配字符串“My name is John”。group(1)返回第一个子组——匹配文本中的"John"。


text = "My name is John"
pattern = "My name is (\w+)"

result1 = re.search(pattern, text)
print(result1.group())
print(result1.group(1))  # 输出结果为"John"
print('=========================================')

# 使用group()返回所有子组
# 在这个示例中，正则表达式"My name is (\w+) (\w+)“匹配字符串"My name is John Doe”。
# group()函数返回整个匹配字符串，group(1)返回第一个子组——“John”，group(2)返回第二个子组——“Doe”。
# groups()函数将所有子组打包成一个元组，以便我们一次性获取它们

text = "My name is John Doe"
pattern = "My name is (\w+) (\w+)"

result = re.search(pattern, text)
print(result.groups())  # 输出结果为("John", "Doe")
