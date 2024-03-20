"""
这两条请求语句使用了不同的参数传递方式，有以下区别：

1. `requests.post(url='http://xx.8.84.xx:8000/inference', json=data)`
   这个语句使用了 `json` 参数，它会自动将提供的 Python 对象（在这里是 `data`）转换为 JSON 格式，
   并把它作为请求的主体内容发送给服务器。这通常用于向服务器发送 JSON 数据。

2. `requests.post(url='http://xx.8.84xx:8000/inference', data=data)`
   这个语句使用了 `data` 参数，它会将提供的字符串（在这里是 `data`）直接作为请求的主体内容发送给服务器。这通常用于向服务器发送表单数据。

所以，两者的区别在于参数的类型和处理方式。如果你的服务器端期望 JSON 格式的数据，你应该使用第一种方式；如果服务器端期望表单数据，则可以使用第二种方式。


1. 使用data作为主体参数

当request的请求头的数据格式为Content-Type=application/json，表明需要传入的data参数的格式应为json。
json是一种文本序列化格式，可以使用json.dumps()方法将字典转成json格式：

data = {
        "layer_tag":"im_index",
        "is_not_need_expt_ver":False,
        "is_not_need_submit":False,
        "user_list":[
            {
                "client_type":0,
                "client_id":"123456"
            }
                    ]
        }

import json
data_json=json.dumps(data)
print(type(data_json))
data_json


可以看到json输出的格式是‘str'，当data为str时，如果不指定content-type，默认为text/plain。

2. 使用json作为主体参数

此时可直接使用字典格式：

import requests
url = 'http://这里填入地址'
headers={'Content-Type':"application/json"}

# 提交请求
# 方法一：使用data参数
r = requests.post(url, headers=headers, data = data_json)

# 方法二：使用json参数
r = requests.post(url, headers=headers, json = data)
不管json是str还是dict，如果不指定headers中的content-type，默认为application/json。


总结：
在通过requests.post()进行POST请求时，传入报文的参数有两个，一个是data，一个是json。 data与json既可以是str类型，也可以是dict类型。

区别：
1、不管json是str还是dict，如果不指定headers中的content-type，默认为application/json

2、data为dict时，如果不指定content-type，默认为application/x-www-form-urlencoded，相当于普通form表单提交的形式

3、data为str时，如果不指定content-type，默认为text/plain

4、json为dict时，如果不指定content-type，默认为application/json

5、json为str时，如果不指定content-type，默认为application/json

6、用data参数提交数据时，request.body的内容则为a=1b=2的这种形式，用json参数提交数据时，request.body的内容则为'{“a”: 1, “b”: 2}’的这种形式

"""


data = {
        "layer_tag":"im_index",
        "is_not_need_expt_ver":False,
        "is_not_need_submit":False,
        "user_list":[
            {
                "client_type":0,
                "client_id":"123456"
            }
                    ]
        }


print(type(data))












