class Solution:
    r"""
    1.11 命名切片
    如果你的程序包含了大量无法直视的硬编码切片，并且你想清理一下代码

    >>> codes = "xxxxxhelloxxxworldxxx"
    >>> hello = slice(5, 10)
    >>> world = slice(13, 18)
    >>> codes[hello]
    'hello'
    >>> codes[world]
    'world'
    """
    def __init__(self):
        pass

    def solve(self):
        pass


if __name__ == '__main__':
    import doctest
    doctest.testmod()