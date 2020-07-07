r"""
9.7 利用装饰器强制函数上的类型检查

inspect.signature
>>> @typeassert(int, int)
... def add(x, y):
...    return x + y
>>> add(1, 2)
3
>>> add(1, '2')
Traceback (most recent call last):
...
TypeError: Argument "y" must be <class 'int'>!


>>> class A:
...     @typeassert(x=int, b=int)
...     def add(self, x, b):
...         return x + b
>>>
>>> a = A()
>>> a.add(1, 2)
3
>>> a.add(1, "2")
3
"""
import functools
import inspect


def typeassert(*ty_args, **ty_kwargs):
    def wrapper(func):
        if not __debug__:
            return func
        # print(__debug__)
        sig = inspect.signature(func)
        bound_types = sig.bind_partial(*ty_args, **ty_kwargs).arguments

        @functools.wraps(func)
        def inner(*args, **kwargs):
            bound_values = sig.bind(*args, **kwargs)
            for name, value in bound_values.arguments.items():
                if name in bound_types:
                    if not isinstance(value, bound_types.get(name)):
                        raise TypeError("Argument \"{}\" must be {!r}!".format(name, bound_types[name]))
            return func(*args, **kwargs)
        return inner
    return wrapper


if __name__ == '__main__':
    import doctest
    doctest.testmod()