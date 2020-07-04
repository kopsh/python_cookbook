class Solution:
    r"""
    7.8 减少可调用对象的参数个数

    >>> def f(a, b, c):
    ...     print(a, b, c)
    >>> from functools import partial
    >>> f1 = partial(f, b=2, c=3)
    >>> f1(1)
    1 2 3
    >>> f1(1, b=3)
    1 3 3
    """
    def __init__(self):
        pass

    def solve(self):
        pass


if __name__ == '__main__':
    import doctest
    doctest.testmod()