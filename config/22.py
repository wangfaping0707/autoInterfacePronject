# import os
#
# g = os.walk('D:\InterAutoTest_W\pymsql_demo')
# print(list(g))
# for path, dir_list, file_list in g:
# #     for dir_name in dir_list:
# #         print(os.path.join(path, dir_name))
# #     for file_name in file_list:
# #         print(os.path.join(path, file_name))
# #
# # print(os.listdir(r'D:\InterAutoTest_W\pymsql_demo'))
# #
# # import datetime
# #
# # def which_day(year, month, date):
# # 	end = datetime.date(year, month, date)
# # 	print(end)  # 2023-12-03
# # 	start = datetime.date(year, 1, 1)
# # 	print(start)  # 2023-01-01
# # 	return (end - start).days + 1
# #
# # print(which_day(2023, 12, 3))
#
#
# class A:
#     def who(self):
#         print('A', end='')
#
# class B(A):
#     def who(self):
#         super(B, self).who()
#         print('B', end='')
#
# class C(A):
#     def who(self):
#         super(C, self).who()
#         print('C', end='')
#
# class D(B, C):
#     def who(self):
#         super(D, self).who()
#         print('D', end='')
#
# item = D()
# item.who()
#
#
# print(D.__mro__)
#
#
# message = 'hello, world!'
# print(message.replace('o', 'O').replace('l', 'L').replace('he', 'HE'))


# import re
#
# message = 'hello, world!'
# pattern = re.compile('[aeiou]')
# print(pattern.sub('#', message))

#
#
# filenames = ['a12.txt', 'a8.txt', 'b10.txt', 'b2.txt', 'b19.txt', 'a3.txt']
#
# filenames.sort()
#
# f= []
# for x in filenames:
# 	f.append(x.replace('a', '').replace('b', '').replace('.txt', ''))
#
# print(f)
# print(sorted(f, key=lambda i:int(i)))


# dict1= {'a':17, 'b':10, 'c':31, 'd':1, 'e':19}
#
# print(
# 	sorted(dict1.items(), key=lambda item: item[1])
# )


class A:
	def __init__(self, value):
		self.__value = value
		print(3344)

	@property
	def value(self):
		print('我执行了。。。。。')
		return self.__value




obj = A(1)
print(dir(obj))

# print(obj.value)

obj.__value = 2
# print(obj.value)
print(obj.__value)



def list_depth(items):
    if isinstance(items, list):
        max_depth = 1
        for item in items:
            max_depth = max(list_depth(item) + 1, max_depth)
        return max_depth
    return 0


l = [1,[4,[433,[443]]]]

print(list_depth(l))

st='fgfgfhgfdhg'
print(reversed(st),type(reversed(st)))



numbers = [1, 2, 3, 4, 5]
reversed_numbers = list(reversed(numbers))
print(reversed_numbers)


string = "Hello, World!"
string_list = list(string)
reversed_string_list = list(reversed(string_list))
reversed_string = "".join(reversed_string_list)
print(reversed_string)

fruits = ("apple", "banana", "orange", "grape")
reversed_fruits = tuple(reversed(fruits))
print(reversed_fruits)


numbers = [1, 2, 3, 4, 5]
for number in reversed(numbers):
	print(number)















