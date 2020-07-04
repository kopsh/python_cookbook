class Solution:
    r"""
    4.3 使用生成器创建新的迭代模式

    使用yield，返回一个生成器
    >>> l = [1, 2, 3]
    >>> g = Solution.solve(l)
    >>> next(g)
    1
    >>> next(g)
    2
    >>> next(g)
    3
    """
    @staticmethod
    def solve(l):
        for i in l:
            yield i


if __name__ == '__main__':
    import doctest
    doctest.testmod()