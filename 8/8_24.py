class Solution:
    r"""
    8.24 让类支持比较操作

    functools.total_ordering
    使用它来装饰一个类，你只需定义一个 __eq__() 方法， 外加其他方法(__lt__, __le__, __gt__, or __ge__)中的一个即可，
    然后装饰器会自动为你填充其它比较方法。
    >>> from functools import total_ordering
    >>> @total_ordering
    ... class A:
    ...     def __init__(self, val):
    ...         self.val = val
    ...     def __eq__(self, other):
    ...         return self.val == other.val
    ...     def __lt__(self, other):
    ...         return self.val < other.val
    >>> a = A(1)
    >>> b = A(2)
    >>> a >= b
    False
    """
    def __init__(self):
        super().__init__()
        pass

    def solve(self):
        pass


if __name__ == '__main__':
    import doctest
    doctest.testmod()