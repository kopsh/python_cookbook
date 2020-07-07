r"""
9.9 将装饰器定义为类
你想使用一个装饰器去包装函数，但是希望返回一个可调用的实例。 你需要让你的装饰器可以同时工作在类定义的内部和外部。

>>> add1(1, 2)
3
>>> add1(2, 3)
5
>>> add1.ncall
2
>>> add2(1, 2)
3
>>> add2.ncall
1
"""

import functools


class Profiled:
    def __init__(self, func):
        functools.wraps(func)(self)
        self.ncall = 0

    def __call__(self, *args, **kwargs):
        self.ncall += 1
        return self.__wrapped__(*args, **kwargs)


@Profiled
def add1(a, b):
    return a+b


@Profiled
def add2(a, b):
    return a+b


class A:
    @Profiled
    def add(self, a, b):
        return a + b


if __name__ == '__main__':
    import doctest
    doctest.testmod()