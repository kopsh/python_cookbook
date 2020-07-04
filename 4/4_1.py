class Solution:
    r"""
    4.1 手动遍历迭代器
    
    >>> l = [1, 2, 3]
    >>> i = iter(l)
    >>> next(i)
    1
    >>> next(i)
    2
    >>> next(i)
    3
    >>> next(i)
    Traceback (most recent call last):
        ...
    StopIteration
    """
    def solve(self):
        pass


if __name__ == '__main__':
    import doctest
    doctest.testmod()