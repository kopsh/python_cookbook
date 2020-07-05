class CheckType:
    r"""
    8.9 创建新的类或实例属性

    使用描述器，实现参数类型检查
    >>> @ParamAssert(a=int, b=list)
    ... class A:
    ...     def __init__(self, a, b):
    ...         self.a = a
    ...         self.b = b
    >>> a = A(1, [])
    """
    def __init__(self, name, expected_type):
        self.name = name
        self.expected_type = expected_type

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError("{} cannot be assigned by {!r}, it`s type is {!r}".format(self.name, value,
                                                                                      self.expected_type))
        instance.__dict__[self.name] = value


class ParamAssert:
    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def __call__(self, cls):
        for name, expected_type in self.kwargs.items():
            setattr(cls, name, CheckType(name, expected_type))
        return cls


class Integer:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return instance.__dict__.get(self.name, None)

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError("{} cannot be assigned by {!r}".format(self.name, value))
        instance.__dict__[self.name] = value


class Point:
    """
    >>> p = Point(0, 0)
    >>> print(p.x)
    0
    >>> p.y = "1"
    Traceback (most recent call last):
    ...
    TypeError: y cannot be assigned by '1'
    """
    x = Integer('x')
    y = Integer('y')

    def __init__(self, x, y):
        self.x = x
        self.y = y

if __name__ == '__main__':
    import doctest
    doctest.testmod()