import requests

url = 'http://www.baidu.com/'
rep = requests.request('GET',url=url)

# 响应内容以文本形式获取
# print(rep.text)
#
# print(rep.content.decode('utf-8'))

# 获取请求头
print(rep.request.headers)
# 获取响应地址
print(rep.url)
# 获取响应头
print(rep.headers)

session = requests.session()
