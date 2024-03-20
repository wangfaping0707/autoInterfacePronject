"""
动态生成参数名称
有时我们需要  动态生成参数名称，例如根据 参数值 来生成一个唯一的标识符。这时可以使用pytest的ids 参数，
它可以指定每个参数值对应的参数名称。例如，我们有一个函数用来测试两个字符串连接后的长度是否正确，可以这样写：

这里我们使用了ids参数，将每个参数值对应的参数名称指定为了一个字符串，分别 是 "字符串长度是否等于10" 和 "字符串长度是否等于15"。
这样，pytest就会在测试结果中显示这些参数名称，方便我们查看和分析测试结果。

"""

from operator import concat

import pytest


@pytest.mark.parametrize("s1, s2, expected", [("hello", "world", 10), ("pytest", "is awesome", 15)],
                         ids=["字符串长度是否等于10", "字符串长度是否等于15"])
def test_len(s1, s2, expected):
	assert len(concat(s1, s2)) == expected
