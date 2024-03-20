import datetime
import json
# 格式化返回的时间
import os
from functools import reduce


# print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
#
# for i in range(1,10):
#     for j in range(1, i+1):
#         print(f'{j}*{i}={j*i}', end=' ')
#     print('\n')
#
# print(reduce(lambda x, y: x * y, [1, 2, 3, 4]))
#
# print(5//3)

# testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
# print(len(testlist)-1)
# testlist.reverse()
# print(testlist)

# list=[]
# for i in range(1, 6):
#     for j in range(1, 6):
#         for k in range(1, 6):
#             if (i != j) and i != k and j != k:
#                 list.append(int(f'{i}{j}{k}'))
#                 # print(f"{i}{j}{k}")
#
#
# print(list)
#
# print(len(list))
# print(os.listdir('.'))

# import random
#
#
# def generate_verification_code():
#     code = ""
#     for i in range(6):
#         code += str(random.randint(0, 9))
#     return code
#
#
# verification_code = generate_verification_code()
# print(verification_code)

import string
chars = string.ascii_letters + string.digits
# print(chars)
#
# list = [99,2,4,5,0,4,46,12,7]
# print(f'排序之前{list}')
#
# # for i in range(len(list)-1):
# #     for j in range(len(list) - i -1):
# #         if list[j]>list[j+1]:
# #             list[j],list[j+1]=list[j+1],list[j]
# #
# #
# # print(f'排序之后{list}')
# #
# #
# #
# #
#
#
# file_text2 = '{"name":"john","age":22,"sex":"woman","address":"USA"}'
# file_text1 = '{"name":"john","age":22,"sex":"man","address":"USA"}'
# dict1 = json.loads(file_text1)
# print(sorted(dict1))
# dict2 = json.loads(file_text2)
# print(sorted(dict2))
#
# print(list(zip(sorted(dict1), sorted(dict2))))
#
# for s1,s2 in zip(sorted(dict1), sorted(dict2)):
#     print(s1,   s2)
#
#
#
# dict1 = {"name": "Alice", "age": 30}
# dict2 = {"city": "New York", "country": "USA"}
# merged_dict = {k: v for k, v in zip(dict1.keys(), dict2.values())}
# print(merged_dict)
#
#
# dict3 = {'a': 1, 'b': 2, 'c': 3}
# dict4 = {'b': 20, 'c': 30, 'd': 40}
# merged_dict1 = {key: value for key, value in zip(dict3, dict4)}
# print(merged_dict1)
#
#
# dict5 = {'a': 1, 'b': 2, 'c': 3}
#
#
# print(list(enumerate('hdfjj')))
#


k = "k:1|k1:2|k2:3|k3:4"
dict1 = {}

print(k.split("|"))


for items in k.split("|"):
    key, value = items.split(":")
    dict1[key] = value



key,value='k:1'.split(':')
print(key,value)

a,b,c = [1,2,3]
print(a,b,c)


