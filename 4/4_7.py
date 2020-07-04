class Solution:
    r"""
    4.7 迭代器切片

    使用itertools.islice
    >>> _iter = iter(range(10))
    >>> import itertools
    >>> for x in itertools.islice(_iter, 5, 10):
    ...     print(x)
    5
    6
    7
    8
    9
    """
    def solve(self):
        pass


if __name__ == '__main__':
    import doctest
    doctest.testmod()