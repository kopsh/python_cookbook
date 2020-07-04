class Solution:
    r"""
    7.12 访问闭包中定义的变量
    >>> def f1():
    ...     n = 0
    ...     def f2():
    ...         print(n)
    ...     def get_n():
    ...         return n
    ...     def set_n(_n):
    ...         nonlocal n
    ...         n = _n
    ...     f2.get_n = get_n
    ...     f2.set_n = set_n
    ...     return f2
    >>> f = f1()
    >>> f()
    0
    >>> f.set_n(20)
    >>> f.get_n()
    20
    """
    def __init__(self):
        pass

    def solve(self):
        pass


if __name__ == '__main__':
    import doctest
    doctest.testmod()