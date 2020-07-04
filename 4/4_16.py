class Solution:
    r"""
    4.16 迭代器代替while无限循环

    >>> l = iter([1, 2, 10, ...])
    >>> for s in iter(lambda: next(l), 10):
    ...     print(s)
    1
    2
    """
    def __init__(self):
        pass

    def solve(self):
        pass


if __name__ == '__main__':
    import doctest
    doctest.testmod()