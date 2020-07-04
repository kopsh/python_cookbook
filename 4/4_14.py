class Solution:
    r"""
    4.14 展开嵌套的序列
    将多层嵌套的容器展开为单层

    >>> l = [1, 2, [3, 4, [5, [6]], 7]]
    >>> list(Solution.solve(l))
    [1, 2, 3, 4, 5, 6, 7]
    """
    @staticmethod
    def solve(_list: list):
        for e in _list:
            if isinstance(e, list):
                yield from Solution.solve(e)
            else:
                yield e


if __name__ == '__main__':
    import doctest
    doctest.testmod()