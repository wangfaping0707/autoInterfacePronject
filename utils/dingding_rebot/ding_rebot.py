import time
import hmac
import hashlib
import base64
import urllib.parse
import requests
from config import setting
"""
hmac是"Hash-based Message Authentication Code"的缩写，它是一种基于哈希函数的消息认证码实现。
在Python中，hmac模块提供了一种简单的方式来生成和验证HMAC，它通常用于需要数据完整性校验的场合，如网络通信、数据加密等。
hmac模块的主要函数：
hmac.new(key[, msg[, digestmod]])：创建一个新的HMAC对象。
hmac.update(msg)：更新HMAC对象的消息。
hmac.digest()：返回HMAC的二进制数字摘要。
hmac.hexdigest()：返回HMAC的十六进制数字摘要。
hmac.copy()：返回HMAC对象的副本。
下面是一个使用hmac模块的例子：
import hmac
# 密钥和消息
key = b'secret-key'
message = b'The quick brown fox jumps over the lazy dog'
# 创建HMAC对象
h = hmac.new(key, message, digestmod='sha256')
# 获取HMAC的十六进制摘要
digest = h.hexdigest()
print(f'HMAC Digest: {digest}')
在这个例子中，我们首先导入hmac模块，然后定义了一个密钥和一条消息。接着，我们使用hmac.new()创建了一个HMAC对象，
指定了密钥和消息，并且使用了'sha256'作为哈希算法。最后，我们调用hexdigest()方法获取了HMAC的十六进制摘要，并打印出来。

"""


def generate_sign():
	"""
	生成签名计算
	:return:
	"""
	# 获取当前时间戳
	timestamp = round(time.time() * 100000)
	# 获取钉钉机器人里面的加签密钥
	secret = setting.secret
	print(secret)
	# 对secret进行编码
	secret_enc = secret.encode('utf-8')
	# 组合当前时间戳 和 编码的 密钥
	str_to_sign = f"{timestamp}\n{secret}"
	# 对组合后的密钥进行编码
	str_to_sign_enc = str_to_sign.encode('utf-8')
	# 通过加密方式 加密当前时间戳和密钥
	hmac_code = hmac.new(secret_enc, str_to_sign_enc, digestmod=hashlib.sha3_256).digest()
	sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
	return timestamp, sign


def send_dd_msg(content, at_all=True):
	"""
	向钉钉群发送群消息
	:param content:  发送的消息内容
	:param at_all:   @全体群成员，默认值为True
	:return:
	"""
	timestamp, sign = generate_sign()
	# 拼接钉钉群发送消息的url
	url = f"{setting.webhook}&timestamp={timestamp}&sign={sign}"
	headers = {'Content-Type': 'application/json;charset=UTF-8'}
	data = {
		'msgtype': 'text',
		'text': {
			'content': content
		},
		'at': {
			'isAtAll': at_all
		}
	}
	res = requests.post(url=url, json=data, headers=headers)
	return res.text

# res = send_dd_msg('你好，up主')
# print(res)
# generate_sign()