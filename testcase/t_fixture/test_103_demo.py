"""
原文链接：https: // blog.csdn.net / m0_60166861 / article / details / 131245874

参数化的组合 :
有时我们需要对多个参数进行组合，例如测试一个函数在不同参数组合下的正确性。
这时可以使用pytest的product参数化，它可以将多个参数值列表进行组合，生成所有可能的参数组合。
例如，我们有一个函数用来测试两个整数相乘的结果是否正确，可以这样写：

这里我们先用两个参数化装饰器分别指定 a和b 的取值范围，然后在测试函数中用 a和b 的乘积来进行断言。
这样，pytest就会自动运行测试函数九次，每次用一个a和一个b的组合来测试函数的正确性。
另外，我们还可以使用product函数来完成同样的功能，它可以将多个参数值列表进行组合，并返回所有可能的参数组合。
"""
from itertools import product
from operator import mul

import pytest


@pytest.mark.parametrize("a", [1, 2, 3])
@pytest.mark.parametrize("b", [4, 5, 6])
def test_mul(a, b):
	assert mul(a, b) == a * b


@pytest.mark.parametrize("a, b", product([1, 2, 3], [4, 5, 6]))
def test_mul2(a, b):
	assert mul(a, b) == a * b


