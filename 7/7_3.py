class Solution:
    r"""
    函数注解

    >>> def add(x: int, y: int) -> int:
    ...     return a + b
    >>> add.__annotations__
    {'x': <class 'int'>, 'y': <class 'int'>, 'return': <class 'int'>}
    """
    def __init__(self):
        pass

    def solve(self):
        pass


if __name__ == '__main__':
    import doctest
    doctest.testmod()