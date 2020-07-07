r"""
9.13 使用元类控制实例的创建

metaclass 以及 __call__

>>> class A(metaclass=Singleton):
...     pass
>>> a = A()
>>> b = A()
>>> a is b
True
>>> class B(metaclass=Cached):
...     def __init__(self, name):
...         self.name = name
...         print("B __init__")
...     def __new__(cls, *args, **kwargs):
...         print("B __new__")
...         return super().__new__(cls)
__Cached __init__
>>> a = B('a')
Cached __call__
B __new__
B __init__
>>> a = B('a')
Cached __call__
"""
import weakref


class Singleton(type):

    def __init__(self, *args, **kwargs):
        self._instance = None
        super().__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        if self._instance:
            return self._instance
        else:
            self._instance = super().__call__(*args, **kwargs)
            return self._instance


class Cached(type):

    def __init__(self, *args, **kwargs):
        self.__cache = weakref.WeakValueDictionary()
        super().__init__(*args, **kwargs)
        print("__Cached __init__")

    def __call__(self, *args):
        print("Cached __call__")
        if args in self.__cache:
            return self.__cache[args]
        else:
            # type(name, bases, dict) -> a new type
            obj = super().__call__(*args)
            self.__cache[args] = obj
            return obj


if __name__ == '__main__':
    import doctest
    doctest.testmod()